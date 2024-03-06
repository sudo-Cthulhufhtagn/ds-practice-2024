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

import grpc
from concurrent import futures

import datetime

class SuggestionService(suggestion_grpc.SuggestionService):
    # Create an RPC function to say hello
    def SuggestionPropose(self, request, context):
        response = suggestion.SuggestionResponse()
        # check only year because why not
        response.suggestion = json.dumps([
            {'bookId': '123', 'title': 'Dummy Book 1', 'author': 'Author 1'},
            {'bookId': '489', 'title': 'Dummy Bookie 3', 'author': 'O. W. Grant'},
            {'bookId': '456', 'title': 'Dummy Book 2', 'author': 'Author 2'}
        ])
        # Return the response object
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