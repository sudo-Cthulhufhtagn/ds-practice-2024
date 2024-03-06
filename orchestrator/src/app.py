from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/fraud_detection'))
sys.path.insert(0, utils_path)
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, utils_path)
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/suggestion'))
sys.path.insert(0, utils_path)
import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc
import suggestion_pb2 as suggestion
import suggestion_pb2_grpc as suggestion_grpc
import json

import grpc

def greet(name='you'):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.HelloServiceStub(channel)
        # Call the service through the stub object.
        response = stub.SayHello(fraud_detection.HelloRequest(name=name))
    return response.greeting

def fraud_check(card_data):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.FraudServiceStub(channel)
        # Call the service through the stub object.
        response = stub.FraudCheck(fraud_detection.FraudRequest(bank_card=card_data))
    return response.status

def transaction_check(data):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        # Create a stub object.
        stub = transaction_verification_grpc.TransactionServiceStub(channel)
        # Call the service through the stub object.
        response = stub.TransactionCheck(transaction_verification.TransactionRequest(expiration_date=data))
    return response.status

def suggestion_request(data):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('suggestion:50053') as channel:
        # Create a stub object.
        stub = suggestion_grpc.SuggestionServiceStub(channel)
        # Call the service through the stub object.
        response = stub.SuggestionPropose(suggestion.SuggestionRequest(input=data))
    return response.suggestion

# Import Flask.
# Flask is a web framework for Python.
# It allows you to build a web application quickly.
# For more information, see https://flask.palletsprojects.com/en/latest/
from flask import Flask, request
from flask_cors import CORS

# Create a simple Flask app.
app = Flask(__name__)
# Enable CORS for the app.
CORS(app)

# Define a GET endpoint.
@app.route('/', methods=['GET'])
def index():
    """
    Responds with 'Hello, [name]' when a GET request is made to '/' endpoint.
    """
    # Test the fraud-detection gRPC service.
    # response = greet(name='orchestrator')
    response = fraud_check('1111222233334444')
    # Return the response.
    return response


@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    # Print request object data
    print("Request Data:", request.json)
    request_parsed = dict(request.json)
    print('0000',request_parsed,'000')
    
    n_services = 3
    codes = [None]*n_services
    with ThreadPoolExecutor(n_services) as e:
        futures_list = []
        # for service in [fraud_check, transaction_check]:
        futures_list.append(e.submit(fraud_check, request_parsed['creditCard']['number']))
        futures_list.append(e.submit(transaction_check, request_parsed['creditCard']['expirationDate']))
        futures_list.append(e.submit(suggestion_request, 'dummy'))
        for i, future in enumerate(futures.as_completed(futures_list)):
            codes[i] = future.result()
            
        
    print('sttt', codes)
    if codes[0]:
        status = "Fraud detected"
    elif codes[1]:
        status = "Transaction failed"
    else:
        status = "Order placed"
        
    # Dummy response following the provided YAML specification for the bookstore
    order_status_response = {
        'orderId': 'random',
        'status': status,
        'orderedBook' : [{ 
                             'title':request_parsed['items'][0]['name'],
                           'pieces': request_parsed['items'][0]['quantity'],
                           'total' : request_parsed['items'][0]['total'],
                            'author' : request_parsed['items'][0]['author']
        }],
        # { 
        #      'bookname':request_parsed['items']['name'],
        #      'bookauthor':request_parsed['items']['author'],
        #      'bookquantity':request_parsed['items']['quantity'],
        #      'booktotal':request_parsed['items']['total']
        # },
        'suggestedBooks': 
                json.loads(codes[i]),
        #     [
        #     {'bookId': '123', 'title': 'Dummy Book 1', 'author': 'Author 1'},
        #     {'bookId': '456', 'title': 'Dummy Book 2', 'author': 'Author 2'}
        # ]

        # Read the contents of request.json
        # print(request.json)

    # Write the contents into output.json


    }
    print(order_status_response)
    return order_status_response


if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
