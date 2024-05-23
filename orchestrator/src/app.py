from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
import sys
import os
import uuid
from prometheus_client import Counter, generate_latest



POST_REQUEST_COUNT = Counter('post_request_count', 'Total number of POST requests')
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
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/queue'))
sys.path.insert(0, utils_path)

import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc
import suggestion_pb2 as suggestion
import suggestion_pb2_grpc as suggestion_grpc
import queue_pb2 as queue
import queue_pb2_grpc as queue_grpc

import json


import grpc

TIKTOK_MAGIC_SWITCH = True

def greet(name='you'):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.HelloServiceStub(channel)
        # Call the service through the stub object.
        response = stub.SayHello(fraud_detection.HelloRequest(name=name))
    return response.greeting

def fraud_check(usernamep, expdatep):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.FraudServiceStub(channel)
        # Call the service through the stub object.
        response = stub.FraudExp(fraud_detection.ExpRequest(ExpDate=expdatep))
        response2 = stub.FraudName(fraud_detection.NameRequest(name=usernamep))
    return response.status or response2.status2

def transaction_books_list(booklist, id, clock):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        # Create a stub object.
        stub = transaction_verification_grpc.TransactionServiceStub(channel)
        # Call the service through the stub object.
        response2 = stub.BookEmpty(transaction_verification.BookRequest(book=booklist, id=id, clock=json.dumps(clock)))
    return response2.status2, response2.id, json.loads(response2.clock)

def transaction_user_date(id, clock, namep, contactp, addressp):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        # Create a stub object.
        stub = transaction_verification_grpc.TransactionServiceStub(channel)
        # Call the service through the stub object.
        response = stub.TransactionCheck(transaction_verification.TransactionRequest(id=id, name=namep, contact=contactp,address=addressp, clock=json.dumps(clock)))
    return response.status, response.id, json.loads(response.clock)

def transaction_card_check(id, clock, cardp):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        # Create a stub object.
        stub = transaction_verification_grpc.TransactionServiceStub(channel)
        # Call the service through the stub object.
        response = stub.CardCheck(transaction_verification.CardRequest(card=cardp, id=id, clock=json.dumps(clock)))
    return response.status3, response.id, json.loads(response.clock)

def fraud_user_check(id, clock, namep):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.FraudServiceStub(channel)
        # Call the service through the stub object.
        response = stub.FraudName(fraud_detection.NameRequest(name=namep, id=id, clock=json.dumps(clock)))
    return response.status2, response.id, json.loads(response.clock)

def fraud_credit_card(id, clock, cardp):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.FraudServiceStub(channel)
        # Call the service through the stub object.
        response = stub.FraudExp(fraud_detection.ExpRequest(ExpDate=cardp, id=id, clock=json.dumps(clock)))
    return response.status, response.id, json.loads(response.clock)

def transaction_check(namep,contactp, addressp, bookp, cardp):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        # Create a stub object.
        stub = transaction_verification_grpc.TransactionServiceStub(channel)
        # Call the service through the stub object.
        response2 = stub.BookEmpty(transaction_verification.BookRequest(book=bookp))
        response = stub.TransactionCheck(transaction_verification.TransactionRequest(name=namep, contact=contactp,address=addressp))
        response3 = stub.CardCheck(transaction_verification.CardRequest(card=cardp))

    return ( response.status or response2.status2 or response3.status3 )

def submit_queue(data, id, len_data):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('queue:50054') as channel:
        # Create a stub object.
        stub = queue_grpc.QueueServiceStub(channel)
        # Call the service through the stub object.
        response = stub.QueuePropose(queue.QueueRequest(input=json.dumps(data), id=id, len_data=len_data))
    return response.status

def suggestion_request(data, id, clock):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('suggestion:50053') as channel:
        # Create a stub object.
        stub = suggestion_grpc.SuggestionServiceStub(channel)
        # Call the service through the stub object.
        response = stub.SuggestionPropose(suggestion.SuggestionRequest(input=data, id=id, clock=json.dumps(clock)))
    return response.suggestion, response.id, json.loads(response.clock)

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
    response = greet(name='orchestrator')
    # Return the response.
    return response


@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; version=0.0.4; charset=utf-8'}



@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    POST_REQUEST_COUNT.inc()

    # Print request object data
    request_parsed = dict(request.json)
    app.logger.info(f"Incoming request with data: {request_parsed}")
    
    n_services = 3
    codes = [None]*n_services

    # NEW stuff    
    order_id = uuid.uuid4().hex
    global_clock = [0]*n_services
    
    # forget elegant threads, SPAGHETTI CODE TIME WOHOOOOOOOOOOOOOOO!
    
    # with ThreadPoolExecutor(n_services) as e:
    #     futures_store = {
    #         e.submit(fraud_check, request_parsed['user']['name'],
    #                  request_parsed['creditCard']['expirationDate']): 0,
    #         e.submit(transaction_check, request_parsed['user']['name'],
    #                  request_parsed['user']['contact'], request_parsed['billingAddress']['zip'],
    #                  request_parsed['items'][0]['name'], request_parsed['creditCard']['number']): 1,
    #         e.submit(suggestion_request, 'dummy'): 2,
    #     }

    #     app.logger.info(f"All microservices requests submitted")
    #     for future in futures.as_completed(futures_store):
    #         codes[futures_store[future]] = future.result()
    
    statusFail = False
    order_traceback = "" 
    
    response, order_id, global_clock = transaction_books_list(request_parsed['items'][0]['name'], order_id, global_clock)
    app.logger.info(f"Transaction Books List response: {response}, order_id: {order_id}, global_clock: {global_clock}")
    
    if response:
        statusFail = True
        order_traceback += "Books list failed; "
    
    response, order_id, global_clock = transaction_user_date(order_id, 
                                                             global_clock, 
                                                             request_parsed['user']['name'], 
                                                             request_parsed['user']['contact'], 
                                                             request_parsed['billingAddress']['zip'])
    
    app.logger.info(f"Transaction User Data response: {response}, order_id: {order_id}, global_clock: {global_clock}")
    
    if response:
        statusFail = True
        order_traceback += "User data failed; "
        
    if TIKTOK_MAGIC_SWITCH:
        global_clock[0] += 1
    
    response, order_id, global_clock = fraud_user_check(
        order_id, global_clock, request_parsed['user']['name'])
    
    app.logger.info(f"Fraud User Check response: {response}, order_id: {order_id}, global_clock: {global_clock}")
    
    if response:
        statusFail = True
        order_traceback += "User fraud failed; "
        
    if TIKTOK_MAGIC_SWITCH:
        global_clock[1] += 1
        
    response, order_id, global_clock = transaction_card_check(
        order_id, global_clock, request_parsed['creditCard']['number'])
    
    app.logger.info(f"Transaction Card Check response: {response}, order_id: {order_id}, global_clock: {global_clock}")
    
    if response:
        statusFail = True
        order_traceback += "Card check failed; "
        
    if TIKTOK_MAGIC_SWITCH:
        global_clock[0] += 1
        
    response, order_id, global_clock = fraud_credit_card(
        order_id, global_clock, request_parsed['creditCard']['number'])
    
    app.logger.info(f"Fraud Credit Card response: {response}, order_id: {order_id}, global_clock: {global_clock}")
    
    if response:
        statusFail = True
        order_traceback += "Card fraud failed; "
        
    if TIKTOK_MAGIC_SWITCH:
        global_clock[1] += 1
    
        
    status = order_traceback if statusFail else "Order placed"
    
       
    app.logger.info(f"Status is fail: {statusFail}, response: {status}, order_id: {order_id}, global_clock: {global_clock}")
    
    suggestios, order_id, global_clock = suggestion_request('dummy', order_id, global_clock)
    
    app.logger.info(f"Suggestions response: {suggestios}, order_id: {order_id}, global_clock: {global_clock}")
            
            
    if not statusFail:
        submit_queue(request_parsed, order_id, len(request_parsed['items']))
        app.logger.info(f"Queue submission order_id: {order_id}")
        status = 'ok'
     
    # app.logger.info(f"All microservices requests completed, results: {codes}")
    # app.logger.info(f"Results: {codes}")
                    
    # if codes[0]:
    #     status = "Fraud detected"
    # elif codes[1]:
    #     status = "Transaction failed"
    # else:
    #     status = "Order placed"
        
    # Dummy response following the provided YAML specification for the bookstore
    order_status_response = {
        'orderId': order_id,
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
                # json.loads(codes[2]), # TODO: uncode
            [
            {'bookId': '123', 'title': 'Dummy Book 1', 'author': 'Author 1'},
            {'bookId': '456', 'title': 'Dummy Book 2', 'author': 'Author 2'}
        ]

        # Read the contents of request.json
        # print(request.json)

    # Write the contents into output.json


    }
    return order_status_response


if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0', debug=True)
