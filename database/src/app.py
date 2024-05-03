import sys
import os
import json
import threading

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/database'))
sys.path.insert(0, utils_path)
import database_pb2 as database
import database_pb2_grpc as database_grpc
import subprocess

import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s")



import grpc
from concurrent import futures
import time
import os

import datetime

# ds-practice-2024-database-2
worker_id = os.popen('curl -s --unix-socket /var/run/docker.sock http://localhost/containers/$HOSTNAME/json | jq -r .Name | xargs').read().strip()
worker_id = int(worker_id.split('-')[-1])

n_workers = 3
local_store = {}

class DatabaseService(database_grpc.DatabaseService):
    # Create an RPC function to say hello
    def DatabaseReader(self, request, context):
        
        inp_key = request.key
        
        # inp is shipped, wohooooo!
        
        logging.info("Database read order: " + inp_key)
        
        logging.info(f"Database storage: {local_store}")
        
        # response = worker_id
        
        
        response = database.DatabaseResponse()
        
        if inp_key == '*':
            response.status = 'ok'
            response.data = json.dumps(local_store)
        elif inp_key in local_store:
            response.status = 'ok'
            logging.info(f"Database reader: {worker_id} read {inp_key} with {local_store[inp_key]}")
            response.data = local_store[inp_key]
        else:
            response.status = 'not found'
            response.data = ''
            
        logging.info(f"Database status {response.status} response: {response.data}")
        
            
        
        return response
    
    def DatabaseWriter(self, request, context):
        
        inp_key = request.key
        inp_data = request.data
        sender_id = request.sender_id
        
        # inp is shipped, wohooooo!
        
        response = database.DatabaseResponse()
        
        logging.info(f"Database storage: {local_store}")
        
        
        if sender_id == 1:
            local_store[inp_key] = inp_data
            logging.info(f"Database writer: {sender_id} wrote {inp_key} with {inp_data}, since came from the Lord")
            response.status = 'ok'
        elif worker_id == 1:
            logging.info('Worker-1 writes to everyone')
            local_store[inp_key] = inp_data
            
            for i in range(2, n_workers+1):
                if i == sender_id:
                    continue
                with grpc.insecure_channel(f'ds-practice-2024-database-{i}:50055') as channel: 
                    stub = database_grpc.DatabaseServiceStub(channel)
                    response = stub.DatabaseWriter(database.DatabaseWrite(key=inp_key, data=inp_data, sender_id=worker_id))                
                    logging.info(f"Database writer: {worker_id} sending to {i} wrote with status {response.status}")
            response.status = 'ok'
        else:
            logging.info(f"Database writer: {worker_id} wrote {inp_key} with {inp_data}, and sent to replica-1")
            
            with grpc.insecure_channel(f'ds-practice-2024-database-1:50055') as channel: 
                stub = database_grpc.DatabaseServiceStub(channel)
                logging.info(f"Database writer: {worker_id} sending to 1-main, wrote with status {response.status}")
                response = stub.DatabaseWriter(database.DatabaseWrite(key=inp_key, data=inp_data, sender_id=worker_id))                
                
            local_store[inp_key] = inp_data
            response.status = 'ok'
        
        logging.info(f"Database storage: {local_store}")
        
        
        return response
    
    def DatabasePreparer(self, request, context):
        
        
        logging.info(f"Database prepared")
        
        
        response = database.DatabaseResponse()
        
        response.status = 'ok'
        
        return response
    
    def DatabaseCommiter(self, request, context):
        
        
        logging.info(f"Database commited")
        
        response = database.DatabaseResponse()
        
        response.status = 'ok'
        
        return response
        
        
 
        
        

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    database_grpc.add_DatabaseServiceServicer_to_server(DatabaseService(), server)
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