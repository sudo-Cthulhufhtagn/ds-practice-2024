import sys
import os
import json

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/suggestion'))
sys.path.insert(0, utils_path)
import suggestion_pb2 as suggestion
import suggestion_pb2_grpc as suggestion_grpc

import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s")



import grpc
from concurrent import futures

import datetime

local_time_keeper = {
    
}
service_identifier = 2

class SuggestionService(suggestion_grpc.SuggestionService):
    # Create an RPC function to say hello
    def SuggestionPropose(self, request, context):
        logging.info("SuggestionPropose request received")
        response = suggestion.SuggestionResponse()
        # get clock
        request_clock = json.loads(request.clock)
        # check if clock is in local_time_keeper
        if request.id not in local_time_keeper:
            logging.info("Clock not found, initializing")
            local_time_keeper[request.id] = request_clock
            
        logging.info("Clock local: " + str(local_time_keeper[request.id]) + " Clock request: " + str(request_clock))
        
        # check only year because why not
        response.suggestion = json.dumps([
            {'bookId': '123', 'title': 'Dummy Book 1', 'author': 'Author 1'},
            {'bookId': '489', 'title': 'Dummy Bookie 3', 'author': 'O. W. Grant'},
            {'bookId': '456', 'title': 'Dummy Book 2', 'author': 'Author 2'}
        ])
        # Return the response object
        logging.info("SuggestionPropose request processed")
        
        local_time_keeper[request.id][service_identifier] += 1
        
        response.clock = json.dumps(local_time_keeper[request.id])
        response.id = request.id
        logging.info("Clock: " + str(local_time_keeper[request.id]))
        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    suggestion_grpc.add_SuggestionServiceServicer_to_server(SuggestionService(), server)
    # Listen on port 50053
    port = "50053"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print("Server started. Listening on port 50053.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()