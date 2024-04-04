# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import executor_pb2 as executor__pb2


class ExecutorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExecutorPropose = channel.unary_unary(
                '/executor.ExecutorService/ExecutorPropose',
                request_serializer=executor__pb2.ExecutorRequest.SerializeToString,
                response_deserializer=executor__pb2.ExecutorResponse.FromString,
                )


class ExecutorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ExecutorPropose(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExecutorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExecutorPropose': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecutorPropose,
                    request_deserializer=executor__pb2.ExecutorRequest.FromString,
                    response_serializer=executor__pb2.ExecutorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'executor.ExecutorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExecutorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ExecutorPropose(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/executor.ExecutorService/ExecutorPropose',
            executor__pb2.ExecutorRequest.SerializeToString,
            executor__pb2.ExecutorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)