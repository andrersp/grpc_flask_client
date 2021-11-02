# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: movies.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='movies.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cmovies.proto\x1a\x1bgoogle/protobuf/empty.proto\"\"\n\x06Genres\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"Q\n\x06Movies\x12\r\n\x05\x61\x64ult\x18\x01 \x01(\x08\x12\x10\n\x08language\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x17\n\x06genres\x18\x04 \x03(\x0b\x32\x07.Genres\"\x1f\n\x04\x44\x61ta\x12\x17\n\x06movies\x18\x01 \x03(\x0b\x32\x07.Movies\"\"\n\x0fMessageResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"<\n\nMoviesData\x12\r\n\x05\x61\x64ult\x18\x01 \x01(\x08\x12\x10\n\x08language\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\")\n\nMoviesList\x12\x1b\n\x06movies\x18\x01 \x03(\x0b\x32\x0b.MoviesData\"\x1b\n\x07MovieId\x12\x10\n\x08movie_id\x18\x01 \x01(\x05\x32\x8f\x01\n\rMoviesService\x12\x32\n\tGetMovies\x12\x16.google.protobuf.Empty\x1a\x0b.MoviesList\"\x00\x12\x1f\n\x08GetMovie\x12\x08.MovieId\x1a\x07.Movies\"\x00\x12)\n\x0cUpdateMovies\x12\x05.Data\x1a\x10.MessageResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_GENRES = _descriptor.Descriptor(
  name='Genres',
  full_name='Genres',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Genres.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Genres.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=79,
)


_MOVIES = _descriptor.Descriptor(
  name='Movies',
  full_name='Movies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adult', full_name='Movies.adult', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='Movies.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='Movies.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genres', full_name='Movies.genres', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=162,
)


_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='movies', full_name='Data.movies', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=195,
)


_MESSAGERESPONSE = _descriptor.Descriptor(
  name='MessageResponse',
  full_name='MessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='MessageResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=231,
)


_MOVIESDATA = _descriptor.Descriptor(
  name='MoviesData',
  full_name='MoviesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='adult', full_name='MoviesData.adult', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='MoviesData.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='MoviesData.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=293,
)


_MOVIESLIST = _descriptor.Descriptor(
  name='MoviesList',
  full_name='MoviesList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='movies', full_name='MoviesList.movies', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=336,
)


_MOVIEID = _descriptor.Descriptor(
  name='MovieId',
  full_name='MovieId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='movie_id', full_name='MovieId.movie_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=365,
)

_MOVIES.fields_by_name['genres'].message_type = _GENRES
_DATA.fields_by_name['movies'].message_type = _MOVIES
_MOVIESLIST.fields_by_name['movies'].message_type = _MOVIESDATA
DESCRIPTOR.message_types_by_name['Genres'] = _GENRES
DESCRIPTOR.message_types_by_name['Movies'] = _MOVIES
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['MessageResponse'] = _MESSAGERESPONSE
DESCRIPTOR.message_types_by_name['MoviesData'] = _MOVIESDATA
DESCRIPTOR.message_types_by_name['MoviesList'] = _MOVIESLIST
DESCRIPTOR.message_types_by_name['MovieId'] = _MOVIEID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Genres = _reflection.GeneratedProtocolMessageType('Genres', (_message.Message,), {
  'DESCRIPTOR' : _GENRES,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:Genres)
  })
_sym_db.RegisterMessage(Genres)

Movies = _reflection.GeneratedProtocolMessageType('Movies', (_message.Message,), {
  'DESCRIPTOR' : _MOVIES,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:Movies)
  })
_sym_db.RegisterMessage(Movies)

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:Data)
  })
_sym_db.RegisterMessage(Data)

MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERESPONSE,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:MessageResponse)
  })
_sym_db.RegisterMessage(MessageResponse)

MoviesData = _reflection.GeneratedProtocolMessageType('MoviesData', (_message.Message,), {
  'DESCRIPTOR' : _MOVIESDATA,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:MoviesData)
  })
_sym_db.RegisterMessage(MoviesData)

MoviesList = _reflection.GeneratedProtocolMessageType('MoviesList', (_message.Message,), {
  'DESCRIPTOR' : _MOVIESLIST,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:MoviesList)
  })
_sym_db.RegisterMessage(MoviesList)

MovieId = _reflection.GeneratedProtocolMessageType('MovieId', (_message.Message,), {
  'DESCRIPTOR' : _MOVIEID,
  '__module__' : 'movies_pb2'
  # @@protoc_insertion_point(class_scope:MovieId)
  })
_sym_db.RegisterMessage(MovieId)



_MOVIESSERVICE = _descriptor.ServiceDescriptor(
  name='MoviesService',
  full_name='MoviesService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=368,
  serialized_end=511,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMovies',
    full_name='MoviesService.GetMovies',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_MOVIESLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMovie',
    full_name='MoviesService.GetMovie',
    index=1,
    containing_service=None,
    input_type=_MOVIEID,
    output_type=_MOVIES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateMovies',
    full_name='MoviesService.UpdateMovies',
    index=2,
    containing_service=None,
    input_type=_DATA,
    output_type=_MESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MOVIESSERVICE)

DESCRIPTOR.services_by_name['MoviesService'] = _MOVIESSERVICE

# @@protoc_insertion_point(module_scope)