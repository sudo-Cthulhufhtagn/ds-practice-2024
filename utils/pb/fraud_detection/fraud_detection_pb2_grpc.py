# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import fraud_detection_pb2 as fraud__detection__pb2


class HelloServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/hello.HelloService/SayHello',
                request_serializer=fraud__detection__pb2.HelloRequest.SerializeToString,
                response_deserializer=fraud__detection__pb2.HelloResponse.FromString,
                )


class HelloServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=fraud__detection__pb2.HelloRequest.FromString,
                    response_serializer=fraud__detection__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.HelloService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HelloService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.HelloService/SayHello',
            fraud__detection__pb2.HelloRequest.SerializeToString,
            fraud__detection__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class FraudServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FraudName = channel.unary_unary(
                '/hello.FraudService/FraudName',
                request_serializer=fraud__detection__pb2.NameRequest.SerializeToString,
                response_deserializer=fraud__detection__pb2.NameResponse.FromString,
                )
        self.FraudExp = channel.unary_unary(
                '/hello.FraudService/FraudExp',
                request_serializer=fraud__detection__pb2.ExpRequest.SerializeToString,
                response_deserializer=fraud__detection__pb2.ExpResponse.FromString,
                )


class FraudServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FraudName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FraudExp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FraudServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FraudName': grpc.unary_unary_rpc_method_handler(
                    servicer.FraudName,
                    request_deserializer=fraud__detection__pb2.NameRequest.FromString,
                    response_serializer=fraud__detection__pb2.NameResponse.SerializeToString,
            ),
            'FraudExp': grpc.unary_unary_rpc_method_handler(
                    servicer.FraudExp,
                    request_deserializer=fraud__detection__pb2.ExpRequest.FromString,
                    response_serializer=fraud__detection__pb2.ExpResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.FraudService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FraudService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FraudName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.FraudService/FraudName',
            fraud__detection__pb2.NameRequest.SerializeToString,
            fraud__detection__pb2.NameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FraudExp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.FraudService/FraudExp',
            fraud__detection__pb2.ExpRequest.SerializeToString,
            fraud__detection__pb2.ExpResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
