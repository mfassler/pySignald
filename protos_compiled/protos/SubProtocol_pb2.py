# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/SubProtocol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/SubProtocol.proto',
  package='textsecure',
  serialized_pb=_b('\n\x18protos/SubProtocol.proto\x12\ntextsecure\"O\n\x17WebSocketRequestMessage\x12\x0c\n\x04verb\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\x0c\x12\n\n\x02id\x18\x04 \x01(\x04\"U\n\x18WebSocketResponseMessage\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06status\x18\x02 \x01(\r\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04\x62ody\x18\x04 \x01(\x0c\"\xe1\x01\n\x10WebSocketMessage\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.textsecure.WebSocketMessage.Type\x12\x34\n\x07request\x18\x02 \x01(\x0b\x32#.textsecure.WebSocketRequestMessage\x12\x36\n\x08response\x18\x03 \x01(\x0b\x32$.textsecure.WebSocketResponseMessage\".\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07REQUEST\x10\x01\x12\x0c\n\x08RESPONSE\x10\x02\x42\x30\n.org.whispersystems.websocket.messages.protobuf')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_WEBSOCKETMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='textsecure.WebSocketMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=388,
  serialized_end=434,
)
_sym_db.RegisterEnumDescriptor(_WEBSOCKETMESSAGE_TYPE)


_WEBSOCKETREQUESTMESSAGE = _descriptor.Descriptor(
  name='WebSocketRequestMessage',
  full_name='textsecure.WebSocketRequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='verb', full_name='textsecure.WebSocketRequestMessage.verb', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='textsecure.WebSocketRequestMessage.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='textsecure.WebSocketRequestMessage.body', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='textsecure.WebSocketRequestMessage.id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=119,
)


_WEBSOCKETRESPONSEMESSAGE = _descriptor.Descriptor(
  name='WebSocketResponseMessage',
  full_name='textsecure.WebSocketResponseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='textsecure.WebSocketResponseMessage.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='textsecure.WebSocketResponseMessage.status', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='textsecure.WebSocketResponseMessage.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='textsecure.WebSocketResponseMessage.body', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=206,
)


_WEBSOCKETMESSAGE = _descriptor.Descriptor(
  name='WebSocketMessage',
  full_name='textsecure.WebSocketMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='textsecure.WebSocketMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request', full_name='textsecure.WebSocketMessage.request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response', full_name='textsecure.WebSocketMessage.response', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WEBSOCKETMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=434,
)

_WEBSOCKETMESSAGE.fields_by_name['type'].enum_type = _WEBSOCKETMESSAGE_TYPE
_WEBSOCKETMESSAGE.fields_by_name['request'].message_type = _WEBSOCKETREQUESTMESSAGE
_WEBSOCKETMESSAGE.fields_by_name['response'].message_type = _WEBSOCKETRESPONSEMESSAGE
_WEBSOCKETMESSAGE_TYPE.containing_type = _WEBSOCKETMESSAGE
DESCRIPTOR.message_types_by_name['WebSocketRequestMessage'] = _WEBSOCKETREQUESTMESSAGE
DESCRIPTOR.message_types_by_name['WebSocketResponseMessage'] = _WEBSOCKETRESPONSEMESSAGE
DESCRIPTOR.message_types_by_name['WebSocketMessage'] = _WEBSOCKETMESSAGE

WebSocketRequestMessage = _reflection.GeneratedProtocolMessageType('WebSocketRequestMessage', (_message.Message,), dict(
  DESCRIPTOR = _WEBSOCKETREQUESTMESSAGE,
  __module__ = 'protos.SubProtocol_pb2'
  # @@protoc_insertion_point(class_scope:textsecure.WebSocketRequestMessage)
  ))
_sym_db.RegisterMessage(WebSocketRequestMessage)

WebSocketResponseMessage = _reflection.GeneratedProtocolMessageType('WebSocketResponseMessage', (_message.Message,), dict(
  DESCRIPTOR = _WEBSOCKETRESPONSEMESSAGE,
  __module__ = 'protos.SubProtocol_pb2'
  # @@protoc_insertion_point(class_scope:textsecure.WebSocketResponseMessage)
  ))
_sym_db.RegisterMessage(WebSocketResponseMessage)

WebSocketMessage = _reflection.GeneratedProtocolMessageType('WebSocketMessage', (_message.Message,), dict(
  DESCRIPTOR = _WEBSOCKETMESSAGE,
  __module__ = 'protos.SubProtocol_pb2'
  # @@protoc_insertion_point(class_scope:textsecure.WebSocketMessage)
  ))
_sym_db.RegisterMessage(WebSocketMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n.org.whispersystems.websocket.messages.protobuf'))
# @@protoc_insertion_point(module_scope)
