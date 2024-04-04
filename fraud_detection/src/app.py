import json
import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/fraud_detection'))
sys.path.insert(0, utils_path)
import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, 
                    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s")

import grpc
import datetime
from concurrent import futures

local_time_keeper = {
    
}
service_identifier = 1

# Create a class to define the server functions, derived from
# fraud_detection_pb2_grpc.HelloServiceServicer
class HelloService(fraud_detection_grpc.HelloServiceServicer):
    # Create an RPC function to say hello
    def SayHello(self, request, context):
        # Create a HelloResponse object
        response = fraud_detection.HelloResponse()
        # Set the greeting field of the response object
        response.greeting = "Hello, " + request.name
        # Print the greeting message
        print(response.greeting)
        # Return the response object
        return response


class FraudService(fraud_detection_grpc.FraudServiceServicer):
    # Create an RPC function to say hello
    def FraudExp(self, request, context):
        logging.info("FraudCheck request received")
        # get clock
        request_clock = json.loads(request.clock)
        
        response = fraud_detection.ExpResponse()
        # check if clock is in local_time_keeper
        if request.id not in local_time_keeper:
            logging.warning("Clock not found, reinitializing")
            local_time_keeper[request.id] = json.loads(request.clock)
            
        logging.info("Clock local: " + str(local_time_keeper[request.id]) + " Clock request: " + str(request_clock))
        # check clock
        if request_clock[service_identifier] >= local_time_keeper[request.id][service_identifier]:
            local_time_keeper[request.id] = request_clock
            # logging the clock
            logging.info("Local clock updated: " + str(local_time_keeper[request.id]))
        else:
            logging.error("Clock not updated, request rejected")
            response.status = True
            response.clock = json.dumps(local_time_keeper[request.id])
            response.id = request.id
            return response
        
        # increment clock
        local_time_keeper[request.id][service_identifier] += 1
        response.clock = json.dumps(local_time_keeper[request.id])
        response.id = request.id
        
        response.status = int(request.ExpDate.split('/')[-1])<int(datetime.datetime.now().strftime("%y")) or\
        (
            int(request.ExpDate.split('/')[-1])==int(datetime.datetime.now().strftime("%y")) and 
            int(request.ExpDate.split('/')[0])<int(datetime.datetime.now().strftime("%m"))
        )
        logging.info("FraudCheck ExpDate request processed, outcome: " + str(response.status))
        # Return the response object
        return response
    
    def FraudName(self, request, context):
        logging.info("FraudCheck request received")
        response2 = fraud_detection.NameResponse()
        # clock log
        request_clock = json.loads(request.clock)
        # clock check
        if request.id not in local_time_keeper:
            logging.warning("Clock not found, reinitializing")
            local_time_keeper[request.id] = json.loads(request.clock)
            
        logging.info("Clock local: " + str(local_time_keeper[request.id]) + " Clock request: " + str(request_clock))
            
        if request_clock[service_identifier] >= local_time_keeper[request.id][service_identifier]:
            local_time_keeper[request.id] = request_clock
            # logging the clock
            logging.info("Local clock updated: " + str(local_time_keeper[request.id]))
        else:
            logging.error("Clock not updated, request rejected")
            response2.status2 = True
            response2.clock = json.dumps(local_time_keeper[request.id])
            response2.id = request.id
            return response2
        
        # increment clock
        local_time_keeper[request.id][service_identifier] += 1
        response2.clock = json.dumps(local_time_keeper[request.id])
        response2.id = request.id
        
        
        response2.status2 = not request.name.isalpha()
        logging.info("FraudCheck name request processed, outcome: " + str(response2.status2))
        # Return the response object
        return response2

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    # fraud_detection_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    fraud_detection_grpc.add_FraudServiceServicer_to_server(FraudService(), server)
    # Listen on port 50051
    port = "50051"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print("Server started. Listening on port 50051.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()