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
import json

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s")

local_time_keeper = {
    
}
service_identifier = 0

class TransactionService(transaction_verification_grpc.TransactionService):
    def BookEmpty(self, request, context):
        logging.info("BookEmpty request received")
        local_time_keeper[request.id] = json.loads(request.clock) # initialize subatomic(vector) clock
        # log the clock
        logging.info("Clock: " + str(local_time_keeper[request.id]))
        response2 = transaction_verification.BookResponse()
        response2.status2 = request.book==""
        local_time_keeper[request.id][service_identifier] += 1
        response2.clock = json.dumps(local_time_keeper[request.id])
        response2.id = request.id
        logging.info("BookEmpty request processed, outcome: " + str(response2.status2))
        # log clock after processing
        logging.info("Clock: " + str(local_time_keeper[request.id]))
        # Return the response object
        return response2
    
    # Create an RPC function to say hello
    def TransactionCheck(self, request, context):
        logging.info("TransactionCheck request received")
        # log clock before processing
        request_clock = json.loads(request.clock)
        logging.info("Clock local: " + str(local_time_keeper[request.id]) + " Clock request: " + str(request_clock))
        
        if request.id not in local_time_keeper:
            logging.warning("Clock not found, reinitializing")
            local_time_keeper[request.id] = json.loads(request.clock)
            
        response = transaction_verification.TransactionResponse()
        
        
        if request_clock[service_identifier] >= local_time_keeper[request.id][service_identifier]:
            local_time_keeper[request.id] = request_clock
            # logging the clock
            logging.info("Local clock updated: " + str(local_time_keeper[request.id]))
        else:
            logging.error("Clock local is greater than request clock, bulshit is happening! The system frauded itself")
            response.status = True # somethings off: everyone is a scam, regardless they admitted it or not
            response.clock = request.clock
            response.id = request.id
            return response
            
        
        
        response.status = bool(request.name=='' and request.contact=='' and request.address=='')
        logging.info("TransactionCheck request processed, outcome: " + str(response.status))
        # increment the clock
        local_time_keeper[request.id][service_identifier] += 1
        response.clock = json.dumps(local_time_keeper[request.id])
        response.id = request.id
        # log clock 
        logging.info("Clock: " + str(local_time_keeper[request.id]))
        # Return the response object
        return response
    
    
    
    def CardCheck(self, request, context):
        logging.info("CardCheck request received")
        response3 = transaction_verification.CardResponse()
        # clock log
        request_clock = json.loads(request.clock)
        logging.info("Clock local: " + str(local_time_keeper[request.id]) + " Clock request: " + str(request_clock))
        # clock check
        if request.id not in local_time_keeper:
            logging.warning("Clock not found, reinitializing")
            local_time_keeper[request.id] = json.loads(request.clock)
            
        if request_clock[service_identifier] >= local_time_keeper[request.id][service_identifier]:
            local_time_keeper[request.id] = request_clock
            # logging the clock
            logging.info("Local clock updated: " + str(local_time_keeper[request.id]))
        else:
            logging.error("Clock local is greater than request clock, bulshit is happening! The system frauded itself")
            response3.status3 = True
            response3.clock = request.clock
            response3.id = request.id
            return response3
        
        response3.status3 = request.card.isnumeric() and len(request.card) == 16
        response3.status3 = not response3.status3
        logging.info("CardCheck request processed, outcome: " + str(response3.status3))
        # update the clock
        local_time_keeper[request.id][service_identifier] += 1
        response3.clock = json.dumps(local_time_keeper[request.id])
        response3.id = request.id
        # log clock
        logging.info("Clock: " + str(local_time_keeper[request.id]))
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