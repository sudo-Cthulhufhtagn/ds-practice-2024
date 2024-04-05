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
        
        response = executore.ExecutorResponse()
        
        response.status = 'ok'
        response.id = request.id
        
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