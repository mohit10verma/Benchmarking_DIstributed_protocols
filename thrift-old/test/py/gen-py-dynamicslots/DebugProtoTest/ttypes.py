#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:dynamic,slots
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.protocol.TBase import TBase, TExceptionBase, TTransport


class SomeEnum(TBase):
  ONE = 1
  TWO = 2

  _VALUES_TO_NAMES = {
    1: "ONE",
    2: "TWO",
  }

  _NAMES_TO_VALUES = {
    "ONE": 1,
    "TWO": 2,
  }


class Doubles(TBase):
  """
  Attributes:
   - nan
   - inf
   - neginf
   - repeating
   - big
   - tiny
   - zero
   - negzero
  """

  __slots__ = [ 
    'nan',
    'inf',
    'neginf',
    'repeating',
    'big',
    'tiny',
    'zero',
    'negzero',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.DOUBLE, 'nan', None, None, ), # 1
    (2, TType.DOUBLE, 'inf', None, None, ), # 2
    (3, TType.DOUBLE, 'neginf', None, None, ), # 3
    (4, TType.DOUBLE, 'repeating', None, None, ), # 4
    (5, TType.DOUBLE, 'big', None, None, ), # 5
    (6, TType.DOUBLE, 'tiny', None, None, ), # 6
    (7, TType.DOUBLE, 'zero', None, None, ), # 7
    (8, TType.DOUBLE, 'negzero', None, None, ), # 8
  )

  def __init__(self, nan=None, inf=None, neginf=None, repeating=None, big=None, tiny=None, zero=None, negzero=None,):
    self.nan = nan
    self.inf = inf
    self.neginf = neginf
    self.repeating = repeating
    self.big = big
    self.tiny = tiny
    self.zero = zero
    self.negzero = negzero

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.nan)
    value = (value * 31) ^ hash(self.inf)
    value = (value * 31) ^ hash(self.neginf)
    value = (value * 31) ^ hash(self.repeating)
    value = (value * 31) ^ hash(self.big)
    value = (value * 31) ^ hash(self.tiny)
    value = (value * 31) ^ hash(self.zero)
    value = (value * 31) ^ hash(self.negzero)
    return value


class OneOfEach(TBase):
  """
  Attributes:
   - im_true
   - im_false
   - a_bite
   - integer16
   - integer32
   - integer64
   - double_precision
   - some_characters
   - zomg_unicode
   - what_who
   - base64
   - byte_list
   - i16_list
   - i64_list
  """

  __slots__ = [ 
    'im_true',
    'im_false',
    'a_bite',
    'integer16',
    'integer32',
    'integer64',
    'double_precision',
    'some_characters',
    'zomg_unicode',
    'what_who',
    'base64',
    'byte_list',
    'i16_list',
    'i64_list',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'im_true', None, None, ), # 1
    (2, TType.BOOL, 'im_false', None, None, ), # 2
    (3, TType.BYTE, 'a_bite', None, 127, ), # 3
    (4, TType.I16, 'integer16', None, 32767, ), # 4
    (5, TType.I32, 'integer32', None, None, ), # 5
    (6, TType.I64, 'integer64', None, 10000000000, ), # 6
    (7, TType.DOUBLE, 'double_precision', None, None, ), # 7
    (8, TType.STRING, 'some_characters', None, None, ), # 8
    (9, TType.STRING, 'zomg_unicode', None, None, ), # 9
    (10, TType.BOOL, 'what_who', None, None, ), # 10
    (11, TType.STRING, 'base64', None, None, ), # 11
    (12, TType.LIST, 'byte_list', (TType.BYTE,None), [
      1,
      2,
      3,
    ], ), # 12
    (13, TType.LIST, 'i16_list', (TType.I16,None), [
      1,
      2,
      3,
    ], ), # 13
    (14, TType.LIST, 'i64_list', (TType.I64,None), [
      1,
      2,
      3,
    ], ), # 14
  )

  def __init__(self, im_true=None, im_false=None, a_bite=thrift_spec[3][4], integer16=thrift_spec[4][4], integer32=None, integer64=thrift_spec[6][4], double_precision=None, some_characters=None, zomg_unicode=None, what_who=None, base64=None, byte_list=thrift_spec[12][4], i16_list=thrift_spec[13][4], i64_list=thrift_spec[14][4],):
    self.im_true = im_true
    self.im_false = im_false
    self.a_bite = a_bite
    self.integer16 = integer16
    self.integer32 = integer32
    self.integer64 = integer64
    self.double_precision = double_precision
    self.some_characters = some_characters
    self.zomg_unicode = zomg_unicode
    self.what_who = what_who
    self.base64 = base64
    if byte_list is self.thrift_spec[12][4]:
      byte_list = [
      1,
      2,
      3,
    ]
    self.byte_list = byte_list
    if i16_list is self.thrift_spec[13][4]:
      i16_list = [
      1,
      2,
      3,
    ]
    self.i16_list = i16_list
    if i64_list is self.thrift_spec[14][4]:
      i64_list = [
      1,
      2,
      3,
    ]
    self.i64_list = i64_list

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.im_true)
    value = (value * 31) ^ hash(self.im_false)
    value = (value * 31) ^ hash(self.a_bite)
    value = (value * 31) ^ hash(self.integer16)
    value = (value * 31) ^ hash(self.integer32)
    value = (value * 31) ^ hash(self.integer64)
    value = (value * 31) ^ hash(self.double_precision)
    value = (value * 31) ^ hash(self.some_characters)
    value = (value * 31) ^ hash(self.zomg_unicode)
    value = (value * 31) ^ hash(self.what_who)
    value = (value * 31) ^ hash(self.base64)
    value = (value * 31) ^ hash(self.byte_list)
    value = (value * 31) ^ hash(self.i16_list)
    value = (value * 31) ^ hash(self.i64_list)
    return value


class Bonk(TBase):
  """
  Attributes:
   - type
   - message
  """

  __slots__ = [ 
    'type',
    'message',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.STRING, 'message', None, None, ), # 2
  )

  def __init__(self, type=None, message=None,):
    self.type = type
    self.message = message

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.message)
    return value


class Nesting(TBase):
  """
  Attributes:
   - my_bonk
   - my_ooe
  """

  __slots__ = [ 
    'my_bonk',
    'my_ooe',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'my_bonk', (Bonk, Bonk.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'my_ooe', (OneOfEach, OneOfEach.thrift_spec), None, ), # 2
  )

  def __init__(self, my_bonk=None, my_ooe=None,):
    self.my_bonk = my_bonk
    self.my_ooe = my_ooe

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.my_bonk)
    value = (value * 31) ^ hash(self.my_ooe)
    return value


class HolyMoley(TBase):
  """
  Attributes:
   - big
   - contain
   - bonks
  """

  __slots__ = [ 
    'big',
    'contain',
    'bonks',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'big', (TType.STRUCT,(OneOfEach, OneOfEach.thrift_spec)), None, ), # 1
    (2, TType.SET, 'contain', (TType.LIST,(TType.STRING,None)), None, ), # 2
    (3, TType.MAP, 'bonks', (TType.STRING,None,TType.LIST,(TType.STRUCT,(Bonk, Bonk.thrift_spec))), None, ), # 3
  )

  def __init__(self, big=None, contain=None, bonks=None,):
    self.big = big
    self.contain = contain
    self.bonks = bonks

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.big)
    value = (value * 31) ^ hash(self.contain)
    value = (value * 31) ^ hash(self.bonks)
    return value


class Backwards(TBase):
  """
  Attributes:
   - first_tag2
   - second_tag1
  """

  __slots__ = [ 
    'second_tag1',
    'first_tag2',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'second_tag1', None, None, ), # 1
    (2, TType.I32, 'first_tag2', None, None, ), # 2
  )

  def __init__(self, first_tag2=None, second_tag1=None,):
    self.first_tag2 = first_tag2
    self.second_tag1 = second_tag1

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.first_tag2)
    value = (value * 31) ^ hash(self.second_tag1)
    return value


class Empty(TBase):

  __slots__ = [ 
   ]

  thrift_spec = (
  )

  def __hash__(self):
    value = 17
    return value


class Wrapper(TBase):
  """
  Attributes:
   - foo
  """

  __slots__ = [ 
    'foo',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'foo', (Empty, Empty.thrift_spec), None, ), # 1
  )

  def __init__(self, foo=None,):
    self.foo = foo

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.foo)
    return value


class RandomStuff(TBase):
  """
  Attributes:
   - a
   - b
   - c
   - d
   - myintlist
   - maps
   - bigint
   - triple
  """

  __slots__ = [ 
    'a',
    'b',
    'c',
    'd',
    'myintlist',
    'maps',
    'bigint',
    'triple',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'a', None, None, ), # 1
    (2, TType.I32, 'b', None, None, ), # 2
    (3, TType.I32, 'c', None, None, ), # 3
    (4, TType.I32, 'd', None, None, ), # 4
    (5, TType.LIST, 'myintlist', (TType.I32,None), None, ), # 5
    (6, TType.MAP, 'maps', (TType.I32,None,TType.STRUCT,(Wrapper, Wrapper.thrift_spec)), None, ), # 6
    (7, TType.I64, 'bigint', None, None, ), # 7
    (8, TType.DOUBLE, 'triple', None, None, ), # 8
  )

  def __init__(self, a=None, b=None, c=None, d=None, myintlist=None, maps=None, bigint=None, triple=None,):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.myintlist = myintlist
    self.maps = maps
    self.bigint = bigint
    self.triple = triple

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.a)
    value = (value * 31) ^ hash(self.b)
    value = (value * 31) ^ hash(self.c)
    value = (value * 31) ^ hash(self.d)
    value = (value * 31) ^ hash(self.myintlist)
    value = (value * 31) ^ hash(self.maps)
    value = (value * 31) ^ hash(self.bigint)
    value = (value * 31) ^ hash(self.triple)
    return value


class Base64(TBase):
  """
  Attributes:
   - a
   - b1
   - b2
   - b3
   - b4
   - b5
   - b6
  """

  __slots__ = [ 
    'a',
    'b1',
    'b2',
    'b3',
    'b4',
    'b5',
    'b6',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'a', None, None, ), # 1
    (2, TType.STRING, 'b1', None, None, ), # 2
    (3, TType.STRING, 'b2', None, None, ), # 3
    (4, TType.STRING, 'b3', None, None, ), # 4
    (5, TType.STRING, 'b4', None, None, ), # 5
    (6, TType.STRING, 'b5', None, None, ), # 6
    (7, TType.STRING, 'b6', None, None, ), # 7
  )

  def __init__(self, a=None, b1=None, b2=None, b3=None, b4=None, b5=None, b6=None,):
    self.a = a
    self.b1 = b1
    self.b2 = b2
    self.b3 = b3
    self.b4 = b4
    self.b5 = b5
    self.b6 = b6

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.a)
    value = (value * 31) ^ hash(self.b1)
    value = (value * 31) ^ hash(self.b2)
    value = (value * 31) ^ hash(self.b3)
    value = (value * 31) ^ hash(self.b4)
    value = (value * 31) ^ hash(self.b5)
    value = (value * 31) ^ hash(self.b6)
    return value


class CompactProtoTestStruct(TBase):
  """
  Attributes:
   - a_byte
   - a_i16
   - a_i32
   - a_i64
   - a_double
   - a_string
   - a_binary
   - true_field
   - false_field
   - empty_struct_field
   - byte_list
   - i16_list
   - i32_list
   - i64_list
   - double_list
   - string_list
   - binary_list
   - boolean_list
   - struct_list
   - byte_set
   - i16_set
   - i32_set
   - i64_set
   - double_set
   - string_set
   - binary_set
   - boolean_set
   - struct_set
   - byte_byte_map
   - i16_byte_map
   - i32_byte_map
   - i64_byte_map
   - double_byte_map
   - string_byte_map
   - binary_byte_map
   - boolean_byte_map
   - byte_i16_map
   - byte_i32_map
   - byte_i64_map
   - byte_double_map
   - byte_string_map
   - byte_binary_map
   - byte_boolean_map
   - list_byte_map
   - set_byte_map
   - map_byte_map
   - byte_map_map
   - byte_set_map
   - byte_list_map
  """

  __slots__ = [ 
    'a_byte',
    'a_i16',
    'a_i32',
    'a_i64',
    'a_double',
    'a_string',
    'a_binary',
    'true_field',
    'false_field',
    'empty_struct_field',
    'byte_list',
    'i16_list',
    'i32_list',
    'i64_list',
    'double_list',
    'string_list',
    'binary_list',
    'boolean_list',
    'struct_list',
    'byte_set',
    'i16_set',
    'i32_set',
    'i64_set',
    'double_set',
    'string_set',
    'binary_set',
    'boolean_set',
    'struct_set',
    'byte_byte_map',
    'i16_byte_map',
    'i32_byte_map',
    'i64_byte_map',
    'double_byte_map',
    'string_byte_map',
    'binary_byte_map',
    'boolean_byte_map',
    'byte_i16_map',
    'byte_i32_map',
    'byte_i64_map',
    'byte_double_map',
    'byte_string_map',
    'byte_binary_map',
    'byte_boolean_map',
    'list_byte_map',
    'set_byte_map',
    'map_byte_map',
    'byte_map_map',
    'byte_set_map',
    'byte_list_map',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.BYTE, 'a_byte', None, None, ), # 1
    (2, TType.I16, 'a_i16', None, None, ), # 2
    (3, TType.I32, 'a_i32', None, None, ), # 3
    (4, TType.I64, 'a_i64', None, None, ), # 4
    (5, TType.DOUBLE, 'a_double', None, None, ), # 5
    (6, TType.STRING, 'a_string', None, None, ), # 6
    (7, TType.STRING, 'a_binary', None, None, ), # 7
    (8, TType.BOOL, 'true_field', None, None, ), # 8
    (9, TType.BOOL, 'false_field', None, None, ), # 9
    (10, TType.STRUCT, 'empty_struct_field', (Empty, Empty.thrift_spec), None, ), # 10
    (11, TType.LIST, 'byte_list', (TType.BYTE,None), None, ), # 11
    (12, TType.LIST, 'i16_list', (TType.I16,None), None, ), # 12
    (13, TType.LIST, 'i32_list', (TType.I32,None), None, ), # 13
    (14, TType.LIST, 'i64_list', (TType.I64,None), None, ), # 14
    (15, TType.LIST, 'double_list', (TType.DOUBLE,None), None, ), # 15
    (16, TType.LIST, 'string_list', (TType.STRING,None), None, ), # 16
    (17, TType.LIST, 'binary_list', (TType.STRING,None), None, ), # 17
    (18, TType.LIST, 'boolean_list', (TType.BOOL,None), None, ), # 18
    (19, TType.LIST, 'struct_list', (TType.STRUCT,(Empty, Empty.thrift_spec)), None, ), # 19
    (20, TType.SET, 'byte_set', (TType.BYTE,None), None, ), # 20
    (21, TType.SET, 'i16_set', (TType.I16,None), None, ), # 21
    (22, TType.SET, 'i32_set', (TType.I32,None), None, ), # 22
    (23, TType.SET, 'i64_set', (TType.I64,None), None, ), # 23
    (24, TType.SET, 'double_set', (TType.DOUBLE,None), None, ), # 24
    (25, TType.SET, 'string_set', (TType.STRING,None), None, ), # 25
    (26, TType.SET, 'binary_set', (TType.STRING,None), None, ), # 26
    (27, TType.SET, 'boolean_set', (TType.BOOL,None), None, ), # 27
    (28, TType.SET, 'struct_set', (TType.STRUCT,(Empty, Empty.thrift_spec)), None, ), # 28
    (29, TType.MAP, 'byte_byte_map', (TType.BYTE,None,TType.BYTE,None), None, ), # 29
    (30, TType.MAP, 'i16_byte_map', (TType.I16,None,TType.BYTE,None), None, ), # 30
    (31, TType.MAP, 'i32_byte_map', (TType.I32,None,TType.BYTE,None), None, ), # 31
    (32, TType.MAP, 'i64_byte_map', (TType.I64,None,TType.BYTE,None), None, ), # 32
    (33, TType.MAP, 'double_byte_map', (TType.DOUBLE,None,TType.BYTE,None), None, ), # 33
    (34, TType.MAP, 'string_byte_map', (TType.STRING,None,TType.BYTE,None), None, ), # 34
    (35, TType.MAP, 'binary_byte_map', (TType.STRING,None,TType.BYTE,None), None, ), # 35
    (36, TType.MAP, 'boolean_byte_map', (TType.BOOL,None,TType.BYTE,None), None, ), # 36
    (37, TType.MAP, 'byte_i16_map', (TType.BYTE,None,TType.I16,None), None, ), # 37
    (38, TType.MAP, 'byte_i32_map', (TType.BYTE,None,TType.I32,None), None, ), # 38
    (39, TType.MAP, 'byte_i64_map', (TType.BYTE,None,TType.I64,None), None, ), # 39
    (40, TType.MAP, 'byte_double_map', (TType.BYTE,None,TType.DOUBLE,None), None, ), # 40
    (41, TType.MAP, 'byte_string_map', (TType.BYTE,None,TType.STRING,None), None, ), # 41
    (42, TType.MAP, 'byte_binary_map', (TType.BYTE,None,TType.STRING,None), None, ), # 42
    (43, TType.MAP, 'byte_boolean_map', (TType.BYTE,None,TType.BOOL,None), None, ), # 43
    (44, TType.MAP, 'list_byte_map', (TType.LIST,(TType.BYTE,None),TType.BYTE,None), None, ), # 44
    (45, TType.MAP, 'set_byte_map', (TType.SET,(TType.BYTE,None),TType.BYTE,None), None, ), # 45
    (46, TType.MAP, 'map_byte_map', (TType.MAP,(TType.BYTE,None,TType.BYTE,None),TType.BYTE,None), None, ), # 46
    (47, TType.MAP, 'byte_map_map', (TType.BYTE,None,TType.MAP,(TType.BYTE,None,TType.BYTE,None)), None, ), # 47
    (48, TType.MAP, 'byte_set_map', (TType.BYTE,None,TType.SET,(TType.BYTE,None)), None, ), # 48
    (49, TType.MAP, 'byte_list_map', (TType.BYTE,None,TType.LIST,(TType.BYTE,None)), None, ), # 49
  )

  def __init__(self, a_byte=None, a_i16=None, a_i32=None, a_i64=None, a_double=None, a_string=None, a_binary=None, true_field=None, false_field=None, empty_struct_field=None, byte_list=None, i16_list=None, i32_list=None, i64_list=None, double_list=None, string_list=None, binary_list=None, boolean_list=None, struct_list=None, byte_set=None, i16_set=None, i32_set=None, i64_set=None, double_set=None, string_set=None, binary_set=None, boolean_set=None, struct_set=None, byte_byte_map=None, i16_byte_map=None, i32_byte_map=None, i64_byte_map=None, double_byte_map=None, string_byte_map=None, binary_byte_map=None, boolean_byte_map=None, byte_i16_map=None, byte_i32_map=None, byte_i64_map=None, byte_double_map=None, byte_string_map=None, byte_binary_map=None, byte_boolean_map=None, list_byte_map=None, set_byte_map=None, map_byte_map=None, byte_map_map=None, byte_set_map=None, byte_list_map=None,):
    self.a_byte = a_byte
    self.a_i16 = a_i16
    self.a_i32 = a_i32
    self.a_i64 = a_i64
    self.a_double = a_double
    self.a_string = a_string
    self.a_binary = a_binary
    self.true_field = true_field
    self.false_field = false_field
    self.empty_struct_field = empty_struct_field
    self.byte_list = byte_list
    self.i16_list = i16_list
    self.i32_list = i32_list
    self.i64_list = i64_list
    self.double_list = double_list
    self.string_list = string_list
    self.binary_list = binary_list
    self.boolean_list = boolean_list
    self.struct_list = struct_list
    self.byte_set = byte_set
    self.i16_set = i16_set
    self.i32_set = i32_set
    self.i64_set = i64_set
    self.double_set = double_set
    self.string_set = string_set
    self.binary_set = binary_set
    self.boolean_set = boolean_set
    self.struct_set = struct_set
    self.byte_byte_map = byte_byte_map
    self.i16_byte_map = i16_byte_map
    self.i32_byte_map = i32_byte_map
    self.i64_byte_map = i64_byte_map
    self.double_byte_map = double_byte_map
    self.string_byte_map = string_byte_map
    self.binary_byte_map = binary_byte_map
    self.boolean_byte_map = boolean_byte_map
    self.byte_i16_map = byte_i16_map
    self.byte_i32_map = byte_i32_map
    self.byte_i64_map = byte_i64_map
    self.byte_double_map = byte_double_map
    self.byte_string_map = byte_string_map
    self.byte_binary_map = byte_binary_map
    self.byte_boolean_map = byte_boolean_map
    self.list_byte_map = list_byte_map
    self.set_byte_map = set_byte_map
    self.map_byte_map = map_byte_map
    self.byte_map_map = byte_map_map
    self.byte_set_map = byte_set_map
    self.byte_list_map = byte_list_map

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.a_byte)
    value = (value * 31) ^ hash(self.a_i16)
    value = (value * 31) ^ hash(self.a_i32)
    value = (value * 31) ^ hash(self.a_i64)
    value = (value * 31) ^ hash(self.a_double)
    value = (value * 31) ^ hash(self.a_string)
    value = (value * 31) ^ hash(self.a_binary)
    value = (value * 31) ^ hash(self.true_field)
    value = (value * 31) ^ hash(self.false_field)
    value = (value * 31) ^ hash(self.empty_struct_field)
    value = (value * 31) ^ hash(self.byte_list)
    value = (value * 31) ^ hash(self.i16_list)
    value = (value * 31) ^ hash(self.i32_list)
    value = (value * 31) ^ hash(self.i64_list)
    value = (value * 31) ^ hash(self.double_list)
    value = (value * 31) ^ hash(self.string_list)
    value = (value * 31) ^ hash(self.binary_list)
    value = (value * 31) ^ hash(self.boolean_list)
    value = (value * 31) ^ hash(self.struct_list)
    value = (value * 31) ^ hash(self.byte_set)
    value = (value * 31) ^ hash(self.i16_set)
    value = (value * 31) ^ hash(self.i32_set)
    value = (value * 31) ^ hash(self.i64_set)
    value = (value * 31) ^ hash(self.double_set)
    value = (value * 31) ^ hash(self.string_set)
    value = (value * 31) ^ hash(self.binary_set)
    value = (value * 31) ^ hash(self.boolean_set)
    value = (value * 31) ^ hash(self.struct_set)
    value = (value * 31) ^ hash(self.byte_byte_map)
    value = (value * 31) ^ hash(self.i16_byte_map)
    value = (value * 31) ^ hash(self.i32_byte_map)
    value = (value * 31) ^ hash(self.i64_byte_map)
    value = (value * 31) ^ hash(self.double_byte_map)
    value = (value * 31) ^ hash(self.string_byte_map)
    value = (value * 31) ^ hash(self.binary_byte_map)
    value = (value * 31) ^ hash(self.boolean_byte_map)
    value = (value * 31) ^ hash(self.byte_i16_map)
    value = (value * 31) ^ hash(self.byte_i32_map)
    value = (value * 31) ^ hash(self.byte_i64_map)
    value = (value * 31) ^ hash(self.byte_double_map)
    value = (value * 31) ^ hash(self.byte_string_map)
    value = (value * 31) ^ hash(self.byte_binary_map)
    value = (value * 31) ^ hash(self.byte_boolean_map)
    value = (value * 31) ^ hash(self.list_byte_map)
    value = (value * 31) ^ hash(self.set_byte_map)
    value = (value * 31) ^ hash(self.map_byte_map)
    value = (value * 31) ^ hash(self.byte_map_map)
    value = (value * 31) ^ hash(self.byte_set_map)
    value = (value * 31) ^ hash(self.byte_list_map)
    return value


class SingleMapTestStruct(TBase):
  """
  Attributes:
   - i32_map
  """

  __slots__ = [ 
    'i32_map',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'i32_map', (TType.I32,None,TType.I32,None), None, ), # 1
  )

  def __init__(self, i32_map=None,):
    self.i32_map = i32_map

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.i32_map)
    return value


class ExceptionWithAMap(TExceptionBase):
  """
  Attributes:
   - blah
   - map_field
  """

  __slots__ = [ 
    'blah',
    'map_field',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'blah', None, None, ), # 1
    (2, TType.MAP, 'map_field', (TType.STRING,None,TType.STRING,None), None, ), # 2
  )

  def __init__(self, blah=None, map_field=None,):
    self.blah = blah
    self.map_field = map_field

  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.blah)
    value = (value * 31) ^ hash(self.map_field)
    return value


class BlowUp(TBase):
  """
  Attributes:
   - b1
   - b2
   - b3
   - b4
  """

  __slots__ = [ 
    'b1',
    'b2',
    'b3',
    'b4',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'b1', (TType.LIST,(TType.I32,None),TType.SET,(TType.MAP,(TType.I32,None,TType.STRING,None))), None, ), # 1
    (2, TType.MAP, 'b2', (TType.LIST,(TType.I32,None),TType.SET,(TType.MAP,(TType.I32,None,TType.STRING,None))), None, ), # 2
    (3, TType.MAP, 'b3', (TType.LIST,(TType.I32,None),TType.SET,(TType.MAP,(TType.I32,None,TType.STRING,None))), None, ), # 3
    (4, TType.MAP, 'b4', (TType.LIST,(TType.I32,None),TType.SET,(TType.MAP,(TType.I32,None,TType.STRING,None))), None, ), # 4
  )

  def __init__(self, b1=None, b2=None, b3=None, b4=None,):
    self.b1 = b1
    self.b2 = b2
    self.b3 = b3
    self.b4 = b4

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.b1)
    value = (value * 31) ^ hash(self.b2)
    value = (value * 31) ^ hash(self.b3)
    value = (value * 31) ^ hash(self.b4)
    return value


class ReverseOrderStruct(TBase):
  """
  Attributes:
   - first
   - second
   - third
   - fourth
  """

  __slots__ = [ 
    'fourth',
    'third',
    'second',
    'first',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'fourth', None, None, ), # 1
    (2, TType.I32, 'third', None, None, ), # 2
    (3, TType.I16, 'second', None, None, ), # 3
    (4, TType.STRING, 'first', None, None, ), # 4
  )

  def __init__(self, first=None, second=None, third=None, fourth=None,):
    self.first = first
    self.second = second
    self.third = third
    self.fourth = fourth

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.first)
    value = (value * 31) ^ hash(self.second)
    value = (value * 31) ^ hash(self.third)
    value = (value * 31) ^ hash(self.fourth)
    return value


class StructWithSomeEnum(TBase):
  """
  Attributes:
   - blah
  """

  __slots__ = [ 
    'blah',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'blah', None, None, ), # 1
  )

  def __init__(self, blah=None,):
    self.blah = blah

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.blah)
    return value


class TestUnion(TBase):
  """
  Attributes:
   - string_field: A doc string
   - i32_field
   - struct_field
   - struct_list
   - other_i32_field
   - enum_field
   - i32_set
   - i32_map
  """

  __slots__ = [ 
    'string_field',
    'i32_field',
    'struct_field',
    'struct_list',
    'other_i32_field',
    'enum_field',
    'i32_set',
    'i32_map',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'string_field', None, None, ), # 1
    (2, TType.I32, 'i32_field', None, None, ), # 2
    (3, TType.STRUCT, 'struct_field', (OneOfEach, OneOfEach.thrift_spec), None, ), # 3
    (4, TType.LIST, 'struct_list', (TType.STRUCT,(RandomStuff, RandomStuff.thrift_spec)), None, ), # 4
    (5, TType.I32, 'other_i32_field', None, None, ), # 5
    (6, TType.I32, 'enum_field', None, None, ), # 6
    (7, TType.SET, 'i32_set', (TType.I32,None), None, ), # 7
    (8, TType.MAP, 'i32_map', (TType.I32,None,TType.I32,None), None, ), # 8
  )

  def __init__(self, string_field=None, i32_field=None, struct_field=None, struct_list=None, other_i32_field=None, enum_field=None, i32_set=None, i32_map=None,):
    self.string_field = string_field
    self.i32_field = i32_field
    self.struct_field = struct_field
    self.struct_list = struct_list
    self.other_i32_field = other_i32_field
    self.enum_field = enum_field
    self.i32_set = i32_set
    self.i32_map = i32_map

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.string_field)
    value = (value * 31) ^ hash(self.i32_field)
    value = (value * 31) ^ hash(self.struct_field)
    value = (value * 31) ^ hash(self.struct_list)
    value = (value * 31) ^ hash(self.other_i32_field)
    value = (value * 31) ^ hash(self.enum_field)
    value = (value * 31) ^ hash(self.i32_set)
    value = (value * 31) ^ hash(self.i32_map)
    return value


class TestUnionMinusStringField(TBase):
  """
  Attributes:
   - i32_field
   - struct_field
   - struct_list
   - other_i32_field
   - enum_field
   - i32_set
   - i32_map
  """

  __slots__ = [ 
    'i32_field',
    'struct_field',
    'struct_list',
    'other_i32_field',
    'enum_field',
    'i32_set',
    'i32_map',
   ]

  thrift_spec = (
    None, # 0
    None, # 1
    (2, TType.I32, 'i32_field', None, None, ), # 2
    (3, TType.STRUCT, 'struct_field', (OneOfEach, OneOfEach.thrift_spec), None, ), # 3
    (4, TType.LIST, 'struct_list', (TType.STRUCT,(RandomStuff, RandomStuff.thrift_spec)), None, ), # 4
    (5, TType.I32, 'other_i32_field', None, None, ), # 5
    (6, TType.I32, 'enum_field', None, None, ), # 6
    (7, TType.SET, 'i32_set', (TType.I32,None), None, ), # 7
    (8, TType.MAP, 'i32_map', (TType.I32,None,TType.I32,None), None, ), # 8
  )

  def __init__(self, i32_field=None, struct_field=None, struct_list=None, other_i32_field=None, enum_field=None, i32_set=None, i32_map=None,):
    self.i32_field = i32_field
    self.struct_field = struct_field
    self.struct_list = struct_list
    self.other_i32_field = other_i32_field
    self.enum_field = enum_field
    self.i32_set = i32_set
    self.i32_map = i32_map

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.i32_field)
    value = (value * 31) ^ hash(self.struct_field)
    value = (value * 31) ^ hash(self.struct_list)
    value = (value * 31) ^ hash(self.other_i32_field)
    value = (value * 31) ^ hash(self.enum_field)
    value = (value * 31) ^ hash(self.i32_set)
    value = (value * 31) ^ hash(self.i32_map)
    return value


class ComparableUnion(TBase):
  """
  Attributes:
   - string_field
   - binary_field
  """

  __slots__ = [ 
    'string_field',
    'binary_field',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'string_field', None, None, ), # 1
    (2, TType.STRING, 'binary_field', None, None, ), # 2
  )

  def __init__(self, string_field=None, binary_field=None,):
    self.string_field = string_field
    self.binary_field = binary_field

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.string_field)
    value = (value * 31) ^ hash(self.binary_field)
    return value


class StructWithAUnion(TBase):
  """
  Attributes:
   - test_union
  """

  __slots__ = [ 
    'test_union',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'test_union', (TestUnion, TestUnion.thrift_spec), None, ), # 1
  )

  def __init__(self, test_union=None,):
    self.test_union = test_union

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.test_union)
    return value


class PrimitiveThenStruct(TBase):
  """
  Attributes:
   - blah
   - blah2
   - bw
  """

  __slots__ = [ 
    'blah',
    'blah2',
    'bw',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'blah', None, None, ), # 1
    (2, TType.I32, 'blah2', None, None, ), # 2
    (3, TType.STRUCT, 'bw', (Backwards, Backwards.thrift_spec), None, ), # 3
  )

  def __init__(self, blah=None, blah2=None, bw=None,):
    self.blah = blah
    self.blah2 = blah2
    self.bw = bw

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.blah)
    value = (value * 31) ^ hash(self.blah2)
    value = (value * 31) ^ hash(self.bw)
    return value


class StructWithASomemap(TBase):
  """
  Attributes:
   - somemap_field
  """

  __slots__ = [ 
    'somemap_field',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'somemap_field', (TType.I32,None,TType.I32,None), None, ), # 1
  )

  def __init__(self, somemap_field=None,):
    self.somemap_field = somemap_field

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.somemap_field)
    return value


class BigFieldIdStruct(TBase):
  """
  Attributes:
   - field1
   - field2
  """

  __slots__ = [ 
    'field1',
    'field2',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'field1', None, None, ), # 1
    None, # 2
    None, # 3
    None, # 4
    None, # 5
    None, # 6
    None, # 7
    None, # 8
    None, # 9
    None, # 10
    None, # 11
    None, # 12
    None, # 13
    None, # 14
    None, # 15
    None, # 16
    None, # 17
    None, # 18
    None, # 19
    None, # 20
    None, # 21
    None, # 22
    None, # 23
    None, # 24
    None, # 25
    None, # 26
    None, # 27
    None, # 28
    None, # 29
    None, # 30
    None, # 31
    None, # 32
    None, # 33
    None, # 34
    None, # 35
    None, # 36
    None, # 37
    None, # 38
    None, # 39
    None, # 40
    None, # 41
    None, # 42
    None, # 43
    None, # 44
    (45, TType.STRING, 'field2', None, None, ), # 45
  )

  def __init__(self, field1=None, field2=None,):
    self.field1 = field1
    self.field2 = field2

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.field1)
    value = (value * 31) ^ hash(self.field2)
    return value


class BreaksRubyCompactProtocol(TBase):
  """
  Attributes:
   - field1
   - field2
   - field3
  """

  __slots__ = [ 
    'field1',
    'field2',
    'field3',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'field1', None, None, ), # 1
    (2, TType.STRUCT, 'field2', (BigFieldIdStruct, BigFieldIdStruct.thrift_spec), None, ), # 2
    (3, TType.I32, 'field3', None, None, ), # 3
  )

  def __init__(self, field1=None, field2=None, field3=None,):
    self.field1 = field1
    self.field2 = field2
    self.field3 = field3

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.field1)
    value = (value * 31) ^ hash(self.field2)
    value = (value * 31) ^ hash(self.field3)
    return value


class TupleProtocolTestStruct(TBase):
  """
  Attributes:
   - field1
   - field2
   - field3
   - field4
   - field5
   - field6
   - field7
   - field8
   - field9
   - field10
   - field11
   - field12
  """

  __slots__ = [ 
    'field12',
    'field11',
    'field10',
    'field9',
    'field8',
    'field7',
    'field6',
    'field5',
    'field4',
    'field3',
    'field2',
    'field1',
   ]

  thrift_spec = None
  def __init__(self, field1=None, field2=None, field3=None, field4=None, field5=None, field6=None, field7=None, field8=None, field9=None, field10=None, field11=None, field12=None,):
    self.field1 = field1
    self.field2 = field2
    self.field3 = field3
    self.field4 = field4
    self.field5 = field5
    self.field6 = field6
    self.field7 = field7
    self.field8 = field8
    self.field9 = field9
    self.field10 = field10
    self.field11 = field11
    self.field12 = field12

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.field1)
    value = (value * 31) ^ hash(self.field2)
    value = (value * 31) ^ hash(self.field3)
    value = (value * 31) ^ hash(self.field4)
    value = (value * 31) ^ hash(self.field5)
    value = (value * 31) ^ hash(self.field6)
    value = (value * 31) ^ hash(self.field7)
    value = (value * 31) ^ hash(self.field8)
    value = (value * 31) ^ hash(self.field9)
    value = (value * 31) ^ hash(self.field10)
    value = (value * 31) ^ hash(self.field11)
    value = (value * 31) ^ hash(self.field12)
    return value


class ListDoublePerf(TBase):
  """
  Attributes:
   - field
  """

  __slots__ = [ 
    'field',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'field', (TType.DOUBLE,None), None, ), # 1
  )

  def __init__(self, field=None,):
    self.field = field

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.field)
    return value
