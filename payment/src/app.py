import sys
import os
import json
import threading

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/payment'))
sys.path.insert(0, utils_path)
import payment_pb2 as payment
import payment_pb2_grpc as payment_grpc
import subprocess

import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s")



import grpc
from concurrent import futures
import time
import os

import datetime

# ds-practice-2024-payment-2
worker_id = os.popen('curl -s --unix-socket /var/run/docker.sock http://localhost/containers/$HOSTNAME/json | jq -r .Name | xargs').read().strip()
worker_id = int(worker_id.split('-')[-1])


class PaymentService(payment_grpc.PaymentService):
    def PaymentPreparer(self, request, context):
        
        
        logging.info(f"Payment prepared")
        
        
        response = payment.PaymentResponse()
        
        response.status = 'ok'
        
        return response
    
    def PaymentCommiter(self, request, context):
        
        
        logging.info(f"Payment commited")
        
        response = payment.PaymentResponse()
        
        response.status = 'ok'
        
        return response
        
        
 
        
        

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    payment_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
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