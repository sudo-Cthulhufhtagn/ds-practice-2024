import sys
import os
import json
import threading

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/queue'))
sys.path.insert(0, utils_path)

utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/executor'))
sys.path.insert(0, utils_path)

import executor_pb2 as executor
import executor_pb2_grpc as executor_grpc

import queue_pb2 as queuee
import queue_pb2_grpc as queue_grpc

import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s")



import grpc
from concurrent import futures
import queue
import time


import datetime

priority_queue = queue.PriorityQueue()

def submit_executor_request(input, id):
    channel = grpc.insecure_channel('executor:50055')
    stub = executor_grpc.ExecutorServiceStub(channel)
    response = stub.ExecutorPropose(executor.ExecutorRequest(input=json.dumps(input), id=id))
    return response

def queue_worker():
    while True:
        if not priority_queue.empty():
            # print("Queue: ", priority_queue.get())
            # logging.info("Queue content: " + str(priority_queue.get()))
            time.sleep(2)
            priority, item, id = priority_queue.get()
            logging.info(f"Submitting request to executor id: {id}")
            response = submit_executor_request(item, id)
            logging.info(f"Executor response: {response.status} for id: {id}")
            time.sleep(10)
            pass

class QueueService(queue_grpc.QueueService):
    # Create an RPC function to say hello
    def QueuePropose(self, request, context):
        
        inp = json.loads(request.input)
        inp_len = request.len_data
        
        priority_queue.put((abs(100-inp_len), inp, request.id))

        logging.info("QueuePropose request put: " + str((abs(100-inp_len), inp, request.id)))
        
        response = queuee.QueueResponse()
        
        response.status = 'ok'
        response.id = request.id
        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    queue_grpc.add_QueueServiceServicer_to_server(QueueService(), server)
    # Listen on port 50053
    port = "50054"
    server.add_insecure_port("[::]:" + port)
    
    threading.Thread(target=queue_worker).start()
    # Start the server
    server.start()
    print(f"Server started. Listening on port {port}.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()