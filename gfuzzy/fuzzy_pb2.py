# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='fuzzy.proto',
  package='gfuzzy',
  serialized_pb='\n\x0b\x66uzzy.proto\x12\x06gfuzzy\"\x15\n\x05Input\x12\x0c\n\x04name\x18\x01 \x02(\t\"L\n\x04Rule\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x12\n\nantecedent\x18\x02 \x02(\t\x12\x12\n\nconsequent\x18\x03 \x02(\t\x12\x0e\n\x06weight\x18\x04 \x01(\x02\"0\n\x03Set\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\t\x12\r\n\x05param\x18\x03 \x03(\x02\"7\n\nConsequent\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0e\n\x06output\x18\x02 \x02(\t\x12\x0b\n\x03set\x18\x03 \x02(\t\"\x16\n\x06Output\x12\x0c\n\x04name\x18\x01 \x02(\t\"\xb2\x01\n\x06System\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1c\n\x05input\x18\x02 \x03(\x0b\x32\r.gfuzzy.Input\x12\x1a\n\x04rule\x18\x03 \x03(\x0b\x32\x0c.gfuzzy.Rule\x12\x18\n\x03set\x18\x04 \x03(\x0b\x32\x0b.gfuzzy.Set\x12&\n\nconsequent\x18\x05 \x03(\x0b\x32\x12.gfuzzy.Consequent\x12\x1e\n\x06output\x18\x06 \x03(\x0b\x32\x0e.gfuzzy.Output')




_INPUT = descriptor.Descriptor(
  name='Input',
  full_name='gfuzzy.Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='gfuzzy.Input.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=23,
  serialized_end=44,
)


_RULE = descriptor.Descriptor(
  name='Rule',
  full_name='gfuzzy.Rule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='gfuzzy.Rule.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='antecedent', full_name='gfuzzy.Rule.antecedent', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='consequent', full_name='gfuzzy.Rule.consequent', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='weight', full_name='gfuzzy.Rule.weight', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=46,
  serialized_end=122,
)


_SET = descriptor.Descriptor(
  name='Set',
  full_name='gfuzzy.Set',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='gfuzzy.Set.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='gfuzzy.Set.type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='param', full_name='gfuzzy.Set.param', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=124,
  serialized_end=172,
)


_CONSEQUENT = descriptor.Descriptor(
  name='Consequent',
  full_name='gfuzzy.Consequent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='gfuzzy.Consequent.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='output', full_name='gfuzzy.Consequent.output', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='set', full_name='gfuzzy.Consequent.set', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=174,
  serialized_end=229,
)


_OUTPUT = descriptor.Descriptor(
  name='Output',
  full_name='gfuzzy.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='gfuzzy.Output.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=231,
  serialized_end=253,
)


_SYSTEM = descriptor.Descriptor(
  name='System',
  full_name='gfuzzy.System',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='gfuzzy.System.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='input', full_name='gfuzzy.System.input', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rule', full_name='gfuzzy.System.rule', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='set', full_name='gfuzzy.System.set', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='consequent', full_name='gfuzzy.System.consequent', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='output', full_name='gfuzzy.System.output', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=256,
  serialized_end=434,
)

_SYSTEM.fields_by_name['input'].message_type = _INPUT
_SYSTEM.fields_by_name['rule'].message_type = _RULE
_SYSTEM.fields_by_name['set'].message_type = _SET
_SYSTEM.fields_by_name['consequent'].message_type = _CONSEQUENT
_SYSTEM.fields_by_name['output'].message_type = _OUTPUT
DESCRIPTOR.message_types_by_name['Input'] = _INPUT
DESCRIPTOR.message_types_by_name['Rule'] = _RULE
DESCRIPTOR.message_types_by_name['Set'] = _SET
DESCRIPTOR.message_types_by_name['Consequent'] = _CONSEQUENT
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['System'] = _SYSTEM

class Input(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INPUT
  
  # @@protoc_insertion_point(class_scope:gfuzzy.Input)

class Rule(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RULE
  
  # @@protoc_insertion_point(class_scope:gfuzzy.Rule)

class Set(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SET
  
  # @@protoc_insertion_point(class_scope:gfuzzy.Set)

class Consequent(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONSEQUENT
  
  # @@protoc_insertion_point(class_scope:gfuzzy.Consequent)

class Output(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OUTPUT
  
  # @@protoc_insertion_point(class_scope:gfuzzy.Output)

class System(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSTEM
  
  # @@protoc_insertion_point(class_scope:gfuzzy.System)

# @@protoc_insertion_point(module_scope)
