# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmain.proto\x12\x12packageandfunction\"2\n\x0c\x66unctionData\x12\x14\n\x0c\x66unctionName\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\"\n\x0bpackageData\x12\x13\n\x0bpackageList\x18\x01 \x03(\t\"$\n\rpackageStatus\x12\x13\n\x0bpackageCode\x18\x01 \x01(\x05\"\x1f\n\x0e\x66unctionResult\x12\r\n\x05reply\x18\x01 \x01(\t2\xb9\x01\n\x0bMainService\x12T\n\x0c\x45xecFunction\x12 .packageandfunction.functionData\x1a\".packageandfunction.functionResult\x12T\n\x0eInstallPackage\x12\x1f.packageandfunction.packageData\x1a!.packageandfunction.packageStatusb\x06proto3')



_FUNCTIONDATA = DESCRIPTOR.message_types_by_name['functionData']
_PACKAGEDATA = DESCRIPTOR.message_types_by_name['packageData']
_PACKAGESTATUS = DESCRIPTOR.message_types_by_name['packageStatus']
_FUNCTIONRESULT = DESCRIPTOR.message_types_by_name['functionResult']
functionData = _reflection.GeneratedProtocolMessageType('functionData', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTIONDATA,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:packageandfunction.functionData)
  })
_sym_db.RegisterMessage(functionData)

packageData = _reflection.GeneratedProtocolMessageType('packageData', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGEDATA,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:packageandfunction.packageData)
  })
_sym_db.RegisterMessage(packageData)

packageStatus = _reflection.GeneratedProtocolMessageType('packageStatus', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGESTATUS,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:packageandfunction.packageStatus)
  })
_sym_db.RegisterMessage(packageStatus)

functionResult = _reflection.GeneratedProtocolMessageType('functionResult', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTIONRESULT,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:packageandfunction.functionResult)
  })
_sym_db.RegisterMessage(functionResult)

_MAINSERVICE = DESCRIPTOR.services_by_name['MainService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FUNCTIONDATA._serialized_start=34
  _FUNCTIONDATA._serialized_end=84
  _PACKAGEDATA._serialized_start=86
  _PACKAGEDATA._serialized_end=120
  _PACKAGESTATUS._serialized_start=122
  _PACKAGESTATUS._serialized_end=158
  _FUNCTIONRESULT._serialized_start=160
  _FUNCTIONRESULT._serialized_end=191
  _MAINSERVICE._serialized_start=194
  _MAINSERVICE._serialized_end=379
# @@protoc_insertion_point(module_scope)
