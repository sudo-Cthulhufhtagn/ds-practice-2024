# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fraud_detection.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66raud_detection.proto\x12\x05hello\"6\n\x0bNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05\x63lock\x18\x03 \x01(\t\"8\n\nExpRequest\x12\x0f\n\x07\x45xpDate\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05\x63lock\x18\x03 \x01(\t\":\n\x0cNameResponse\x12\x0f\n\x07status2\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05\x63lock\x18\x03 \x01(\t\"8\n\x0b\x45xpResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\n\n\x02id\x18\x02 \x01(\t\x12\r\n\x05\x63lock\x18\x03 \x01(\t\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\rHelloResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t2E\n\x0cHelloService\x12\x35\n\x08SayHello\x12\x13.hello.HelloRequest\x1a\x14.hello.HelloResponse2w\n\x0c\x46raudService\x12\x34\n\tFraudName\x12\x12.hello.NameRequest\x1a\x13.hello.NameResponse\x12\x31\n\x08\x46raudExp\x12\x11.hello.ExpRequest\x1a\x12.hello.ExpResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fraud_detection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_NAMEREQUEST']._serialized_start=32
  _globals['_NAMEREQUEST']._serialized_end=86
  _globals['_EXPREQUEST']._serialized_start=88
  _globals['_EXPREQUEST']._serialized_end=144
  _globals['_NAMERESPONSE']._serialized_start=146
  _globals['_NAMERESPONSE']._serialized_end=204
  _globals['_EXPRESPONSE']._serialized_start=206
  _globals['_EXPRESPONSE']._serialized_end=262
  _globals['_HELLOREQUEST']._serialized_start=264
  _globals['_HELLOREQUEST']._serialized_end=292
  _globals['_HELLORESPONSE']._serialized_start=294
  _globals['_HELLORESPONSE']._serialized_end=327
  _globals['_HELLOSERVICE']._serialized_start=329
  _globals['_HELLOSERVICE']._serialized_end=398
  _globals['_FRAUDSERVICE']._serialized_start=400
  _globals['_FRAUDSERVICE']._serialized_end=519
# @@protoc_insertion_point(module_scope)
