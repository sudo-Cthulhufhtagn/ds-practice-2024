# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import transaction_verification_pb2 as transaction__verification__pb2


class TransactionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BookEmpty = channel.unary_unary(
                '/transaction.TransactionService/BookEmpty',
                request_serializer=transaction__verification__pb2.BookRequest.SerializeToString,
                response_deserializer=transaction__verification__pb2.BookResponse.FromString,
                )
        self.TransactionCheck = channel.unary_unary(
                '/transaction.TransactionService/TransactionCheck',
                request_serializer=transaction__verification__pb2.TransactionRequest.SerializeToString,
                response_deserializer=transaction__verification__pb2.TransactionResponse.FromString,
                )
        self.CardCheck = channel.unary_unary(
                '/transaction.TransactionService/CardCheck',
                request_serializer=transaction__verification__pb2.CardRequest.SerializeToString,
                response_deserializer=transaction__verification__pb2.CardResponse.FromString,
                )


class TransactionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BookEmpty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransactionCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CardCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransactionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BookEmpty': grpc.unary_unary_rpc_method_handler(
                    servicer.BookEmpty,
                    request_deserializer=transaction__verification__pb2.BookRequest.FromString,
                    response_serializer=transaction__verification__pb2.BookResponse.SerializeToString,
            ),
            'TransactionCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.TransactionCheck,
                    request_deserializer=transaction__verification__pb2.TransactionRequest.FromString,
                    response_serializer=transaction__verification__pb2.TransactionResponse.SerializeToString,
            ),
            'CardCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.CardCheck,
                    request_deserializer=transaction__verification__pb2.CardRequest.FromString,
                    response_serializer=transaction__verification__pb2.CardResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'transaction.TransactionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransactionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BookEmpty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transaction.TransactionService/BookEmpty',
            transaction__verification__pb2.BookRequest.SerializeToString,
            transaction__verification__pb2.BookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransactionCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transaction.TransactionService/TransactionCheck',
            transaction__verification__pb2.TransactionRequest.SerializeToString,
            transaction__verification__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CardCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transaction.TransactionService/CardCheck',
            transaction__verification__pb2.CardRequest.SerializeToString,
            transaction__verification__pb2.CardResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
