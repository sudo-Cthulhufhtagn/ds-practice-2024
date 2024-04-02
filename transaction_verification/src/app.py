import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, utils_path)
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

import grpc
from concurrent import futures
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s")


class TransactionService(transaction_verification_grpc.TransactionService):
    # Create an RPC function to say hello
    def TransactionCheck(self, request, context):
        logging.info("TransactionCheck request received")
        response = transaction_verification.TransactionResponse()
        response.status = bool(request.name=='' and request.contact=='' and request.address=='')
        logging.info("TransactionCheck request processed, outcome: " + str(response.status))
        # Return the response object
        return response
    
    def BookEmpty(self, request, context):
        logging.info("BookEmpty request received")
        response2 = transaction_verification.BookResponse()
        response2.status2 = request.book==""
        logging.info("BookEmpty request processed, outcome: " + str(response2.status2))
        # Return the response object
        return response2
    
    def CardCheck(self, request, context):
        logging.info("CardCheck request received")
        response3 = transaction_verification.CardResponse()
        response3.status3 = request.card.isnumeric() and len(request.card) == 16
        response3.status3 = not response3.status3
        logging.info("CardCheck request processed, outcome: " + str(response3.status3))
        return response3


def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    transaction_verification_grpc.add_TransactionServiceServicer_to_server(TransactionService(), server)
    # Listen on port 50052
    port = "50052"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print("Server started. Listening on port 50052.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()