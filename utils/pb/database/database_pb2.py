# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: database.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x64\x61tabase.proto\x12\x08\x64\x61tabase\"\x1b\n\x0c\x44\x61tabaseRead\x12\x0b\n\x03key\x18\x01 \x01(\t\"=\n\rDatabaseWrite\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x11\n\tsender_id\x18\x03 \x01(\x05\"0\n\x10\x44\x61tabaseResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t2\x9e\x01\n\x0f\x44\x61tabaseService\x12\x44\n\x0e\x44\x61tabaseReader\x12\x16.database.DatabaseRead\x1a\x1a.database.DatabaseResponse\x12\x45\n\x0e\x44\x61tabaseWriter\x12\x17.database.DatabaseWrite\x1a\x1a.database.DatabaseResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'database_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DATABASEREAD']._serialized_start=28
  _globals['_DATABASEREAD']._serialized_end=55
  _globals['_DATABASEWRITE']._serialized_start=57
  _globals['_DATABASEWRITE']._serialized_end=118
  _globals['_DATABASERESPONSE']._serialized_start=120
  _globals['_DATABASERESPONSE']._serialized_end=168
  _globals['_DATABASESERVICE']._serialized_start=171
  _globals['_DATABASESERVICE']._serialized_end=329
# @@protoc_insertion_point(module_scope)
