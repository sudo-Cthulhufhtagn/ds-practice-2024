import sys
import os
import json
import threading

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/executor'))
sys.path.insert(0, utils_path)
import executor_pb2 as executore
import executor_pb2_grpc as executor_grpc
import subprocess

utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/database'))
sys.path.insert(0, utils_path)
import database_pb2 as database
import database_pb2_grpc as database_grpc

utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/payment'))
sys.path.insert(0, utils_path)
import payment_pb2 as payment
import payment_pb2_grpc as payment_grpc

import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s")



import grpc
from concurrent import futures
import time
import os

import datetime





class ExecutorService(executor_grpc.ExecutorService):
    # Create an RPC function to say hello
    def ExecutorPropose(self, request, context):
        
        inp = json.loads(request.input)
        
        # inp is shipped, wohooooo!
        
        logging.info("ExecutorPropose executed order: " + str(request.id))
        
        response = os.popen('curl -s --unix-socket /var/run/docker.sock http://localhost/containers/$HOSTNAME/json | jq -r .Name | xargs').read().strip()
        
        
        logging.info(f"ExecutorPropose worker: {response}")
        
        for item in inp['items']:
            
            with grpc.insecure_channel('database:50055') as channel:
                # Create a stub object.
                stub = database_grpc.DatabaseServiceStub(channel)
                response = stub.DatabaseReader(database.DatabaseRead(key=item['name']))
                if not response.data:
                    number = 10
                else:
                    response = json.loads(response.data)
                    number = response['quantity']
            
        
            with grpc.insecure_channel('database:50055') as channel:
                # Create a stub object.
                stub = database_grpc.DatabaseServiceStub(channel)
                response = stub.DatabaseWriter(database.DatabaseWrite(key=item['name'], data=json.dumps({'quantity': number-1}), sender_id=-1))                
                logging.info(f"ExecutorService sent data to DatabaseService response code: {response.status}")
            
        
        response = executore.ExecutorResponse()
        
        response.status = 'ok'
        response.id = request.id
        
        prepared = True
        with grpc.insecure_channel('database:50055') as channel:
            # Create a stub object.
            logging.info(f"ExecutorService sent Prepare to DatabaseService")
            stub = database_grpc.DatabaseServiceStub(channel)
            response = stub.DatabasePreparer(database.DatabasePrepare(key=item['name']))
            logging.info(f"ExecutorService got Prepare from DatabaseService, status: {response.status}")
            if response.status != 'ok':
                prepared = False
                
        with grpc.insecure_channel('payment:50055') as channel:
            # Create a stub object.
            logging.info(f"ExecutorService sent Prepare to PaymentService")
            stub = payment_grpc.PaymentServiceStub(channel)
            response = stub.PaymentPreparer(payment.PaymentPrepare(key=item['name']))
            logging.info(f"ExecutorService got Prepare from PaymentService, status: {response.status}")
            if response.status != 'ok':
                prepared = False
            
        commited = True
        with grpc.insecure_channel('database:50055') as channel:
            # Create a stub object.
            logging.info(f"ExecutorService sent Prepare to DatabaseService")
            stub = database_grpc.DatabaseServiceStub(channel)
            response = stub.DatabaseCommiter(database.DatabaseCommit(key=item['name']))
            logging.info(f"ExecutorService got Prepare from DatabaseService, status: {response.status}")
            if response.status != 'ok':
                commited = False
                
        with grpc.insecure_channel('payment:50055') as channel:
            # Create a stub object.
            logging.info(f"ExecutorService sent Commit to PaymentService")
            stub = payment_grpc.PaymentServiceStub(channel)
            response = stub.PaymentCommiter(payment.PaymentCommit(key=item['name']))
            logging.info(f"ExecutorService got Commit from PaymentService, status: {response.status}")
            if response.status != 'ok':
                prepared = False
        
        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    executor_grpc.add_ExecutorServiceServicer_to_server(ExecutorService(), server)
    # Listen on port 50053
    port = "50055"
    server.add_insecure_port("[::]:" + port)

    # Start the server
    server.start()
    print(f"Server started. Listening on port {port}.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()