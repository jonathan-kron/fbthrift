#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import folly.iobuf as _fbthrift_iobuf
import thrift.py3.types
import thrift.py3.exceptions
from thrift.py3.types import __NotSet, NOTSET
import typing as _typing
from typing_extensions import Final

import sys
import itertools
import facebook.thrift.annotation.thrift.types as _facebook_thrift_annotation_thrift_types
import apache.thrift.op.patch.types as _apache_thrift_op_patch_types
import apache.thrift.type.standard.types as _apache_thrift_type_standard_types


__property__ = property


class MyEnum(thrift.py3.types.Enum):
    MyValue0: MyEnum = ...
    def _to_python(self) -> "test.fixtures.patch.module.thrift_types.MyEnum": ...   # type: ignore
    def _to_py3(self) -> MyEnum: ...
    def _to_py_deprecated(self) -> int: ...


class MyData(thrift.py3.types.Struct, _typing.Hashable):
    class __fbthrift_IsSet:
        pass

    data1: Final[str] = ...

    data2: Final[int] = ...

    def __init__(
        self, *,
        data1: _typing.Optional[str]=None,
        data2: _typing.Optional[int]=None
    ) -> None: ...

    def __call__(
        self, *,
        data1: _typing.Union[str, '__NotSet', None]=NOTSET,
        data2: _typing.Union[int, '__NotSet', None]=NOTSET
    ) -> MyData: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['MyData'], bytes]]: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'MyData') -> bool: ...
    def __gt__(self, other: 'MyData') -> bool: ...
    def __le__(self, other: 'MyData') -> bool: ...
    def __ge__(self, other: 'MyData') -> bool: ...

    def _to_python(self) -> "test.fixtures.patch.module.thrift_types.MyData": ...   # type: ignore
    def _to_py3(self) -> MyData: ...
    def _to_py_deprecated(self) -> "module.ttypes.MyData": ...   # type: ignore

_InnerUnionValueType = _typing.Union[None, bytes]

class InnerUnion(thrift.py3.types.Union, _typing.Hashable):
    class __fbthrift_IsSet:
        innerOption: bool
        pass

    innerOption: Final[bytes] = ...

    def __init__(
        self, *,
        innerOption: _typing.Optional[bytes]=None
    ) -> None: ...

    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'InnerUnion') -> bool: ...
    def __gt__(self, other: 'InnerUnion') -> bool: ...
    def __le__(self, other: 'InnerUnion') -> bool: ...
    def __ge__(self, other: 'InnerUnion') -> bool: ...

    class Type(thrift.py3.types.Enum):
        EMPTY: InnerUnion.Type = ...
        innerOption: InnerUnion.Type = ...

    @staticmethod
    def fromValue(value: _InnerUnionValueType) -> InnerUnion: ...
    @__property__
    def value(self) -> _InnerUnionValueType: ...
    @__property__
    def type(self) -> "InnerUnion.Type": ...

    def _to_python(self) -> "test.fixtures.patch.module.thrift_types.InnerUnion": ...   # type: ignore
    def _to_py3(self) -> InnerUnion: ...
    def _to_py_deprecated(self) -> "module.ttypes.InnerUnion": ...   # type: ignore

_MyUnionValueType = _typing.Union[None, str, int, InnerUnion]

class MyUnion(thrift.py3.types.Union, _typing.Hashable):
    class __fbthrift_IsSet:
        option1: bool
        option2: bool
        option3: bool
        pass

    option1: Final[str] = ...

    option2: Final[int] = ...

    option3: Final[InnerUnion] = ...

    def __init__(
        self, *,
        option1: _typing.Optional[str]=None,
        option2: _typing.Optional[int]=None,
        option3: _typing.Optional[InnerUnion]=None
    ) -> None: ...

    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'MyUnion') -> bool: ...
    def __gt__(self, other: 'MyUnion') -> bool: ...
    def __le__(self, other: 'MyUnion') -> bool: ...
    def __ge__(self, other: 'MyUnion') -> bool: ...

    class Type(thrift.py3.types.Enum):
        EMPTY: MyUnion.Type = ...
        option1: MyUnion.Type = ...
        option2: MyUnion.Type = ...
        option3: MyUnion.Type = ...

    @staticmethod
    def fromValue(value: _MyUnionValueType) -> MyUnion: ...
    @__property__
    def value(self) -> _MyUnionValueType: ...
    @__property__
    def type(self) -> "MyUnion.Type": ...

    def _to_python(self) -> "test.fixtures.patch.module.thrift_types.MyUnion": ...   # type: ignore
    def _to_py3(self) -> MyUnion: ...
    def _to_py_deprecated(self) -> "module.ttypes.MyUnion": ...   # type: ignore

class MyStruct(thrift.py3.types.Struct, _typing.Hashable):
    class __fbthrift_IsSet:
        optBoolVal: bool
        optByteVal: bool
        optI16Val: bool
        optI32Val: bool
        optI64Val: bool
        optFloatVal: bool
        optDoubleVal: bool
        optStringVal: bool
        optBinaryVal: bool
        optEnumVal: bool
        optStructVal: bool
        optLateStructVal: bool
        optListVal: bool
        optSetVal: bool
        optMapVal: bool
        pass

    boolVal: Final[bool] = ...

    byteVal: Final[int] = ...

    i16Val: Final[int] = ...

    i32Val: Final[int] = ...

    i64Val: Final[int] = ...

    floatVal: Final[float] = ...

    doubleVal: Final[float] = ...

    stringVal: Final[str] = ...

    binaryVal: Final[_fbthrift_iobuf.IOBuf] = ...

    enumVal: Final[MyEnum] = ...

    structVal: Final[MyData] = ...

    unionVal: Final[MyUnion] = ...

    lateStructVal: Final[LateDefStruct] = ...

    durationVal: Final[_apache_thrift_type_standard_types.DurationStruct] = ...

    optBoolVal: Final[_typing.Optional[bool]] = ...

    optByteVal: Final[_typing.Optional[int]] = ...

    optI16Val: Final[_typing.Optional[int]] = ...

    optI32Val: Final[_typing.Optional[int]] = ...

    optI64Val: Final[_typing.Optional[int]] = ...

    optFloatVal: Final[_typing.Optional[float]] = ...

    optDoubleVal: Final[_typing.Optional[float]] = ...

    optStringVal: Final[_typing.Optional[str]] = ...

    optBinaryVal: Final[_typing.Optional[_fbthrift_iobuf.IOBuf]] = ...

    optEnumVal: Final[_typing.Optional[MyEnum]] = ...

    optStructVal: Final[_typing.Optional[MyData]] = ...

    optLateStructVal: Final[_typing.Optional[LateDefStruct]] = ...

    optListVal: Final[_typing.Optional[_typing.Sequence[int]]] = ...

    optSetVal: Final[_typing.Optional[_typing.AbstractSet[str]]] = ...

    optMapVal: Final[_typing.Optional[_typing.Mapping[str, str]]] = ...

    listMap: Final[_typing.Sequence[_typing.Mapping[str, int]]] = ...

    mapMap: Final[_typing.Mapping[str, _typing.Mapping[str, int]]] = ...

    def __init__(
        self, *,
        boolVal: _typing.Optional[bool]=None,
        byteVal: _typing.Optional[int]=None,
        i16Val: _typing.Optional[int]=None,
        i32Val: _typing.Optional[int]=None,
        i64Val: _typing.Optional[int]=None,
        floatVal: _typing.Optional[float]=None,
        doubleVal: _typing.Optional[float]=None,
        stringVal: _typing.Optional[str]=None,
        binaryVal: _typing.Optional[_fbthrift_iobuf.IOBuf]=None,
        enumVal: _typing.Optional[MyEnum]=None,
        structVal: _typing.Optional[MyData]=None,
        unionVal: _typing.Optional[MyUnion]=None,
        lateStructVal: _typing.Optional[LateDefStruct]=None,
        durationVal: _typing.Optional[_apache_thrift_type_standard_types.DurationStruct]=None,
        optBoolVal: _typing.Optional[bool]=None,
        optByteVal: _typing.Optional[int]=None,
        optI16Val: _typing.Optional[int]=None,
        optI32Val: _typing.Optional[int]=None,
        optI64Val: _typing.Optional[int]=None,
        optFloatVal: _typing.Optional[float]=None,
        optDoubleVal: _typing.Optional[float]=None,
        optStringVal: _typing.Optional[str]=None,
        optBinaryVal: _typing.Optional[_fbthrift_iobuf.IOBuf]=None,
        optEnumVal: _typing.Optional[MyEnum]=None,
        optStructVal: _typing.Optional[MyData]=None,
        optLateStructVal: _typing.Optional[LateDefStruct]=None,
        optListVal: _typing.Optional[_typing.Sequence[int]]=None,
        optSetVal: _typing.Optional[_typing.AbstractSet[str]]=None,
        optMapVal: _typing.Optional[_typing.Mapping[str, str]]=None,
        listMap: _typing.Optional[_typing.Sequence[_typing.Mapping[str, int]]]=None,
        mapMap: _typing.Optional[_typing.Mapping[str, _typing.Mapping[str, int]]]=None
    ) -> None: ...

    def __call__(
        self, *,
        boolVal: _typing.Union[bool, '__NotSet', None]=NOTSET,
        byteVal: _typing.Union[int, '__NotSet', None]=NOTSET,
        i16Val: _typing.Union[int, '__NotSet', None]=NOTSET,
        i32Val: _typing.Union[int, '__NotSet', None]=NOTSET,
        i64Val: _typing.Union[int, '__NotSet', None]=NOTSET,
        floatVal: _typing.Union[float, '__NotSet', None]=NOTSET,
        doubleVal: _typing.Union[float, '__NotSet', None]=NOTSET,
        stringVal: _typing.Union[str, '__NotSet', None]=NOTSET,
        binaryVal: _typing.Union[_fbthrift_iobuf.IOBuf, '__NotSet', None]=NOTSET,
        enumVal: _typing.Union[MyEnum, '__NotSet', None]=NOTSET,
        structVal: _typing.Union[MyData, '__NotSet', None]=NOTSET,
        unionVal: _typing.Union[MyUnion, '__NotSet', None]=NOTSET,
        lateStructVal: _typing.Union[LateDefStruct, '__NotSet', None]=NOTSET,
        durationVal: _typing.Union[_apache_thrift_type_standard_types.DurationStruct, '__NotSet', None]=NOTSET,
        optBoolVal: _typing.Union[bool, '__NotSet', None]=NOTSET,
        optByteVal: _typing.Union[int, '__NotSet', None]=NOTSET,
        optI16Val: _typing.Union[int, '__NotSet', None]=NOTSET,
        optI32Val: _typing.Union[int, '__NotSet', None]=NOTSET,
        optI64Val: _typing.Union[int, '__NotSet', None]=NOTSET,
        optFloatVal: _typing.Union[float, '__NotSet', None]=NOTSET,
        optDoubleVal: _typing.Union[float, '__NotSet', None]=NOTSET,
        optStringVal: _typing.Union[str, '__NotSet', None]=NOTSET,
        optBinaryVal: _typing.Union[_fbthrift_iobuf.IOBuf, '__NotSet', None]=NOTSET,
        optEnumVal: _typing.Union[MyEnum, '__NotSet', None]=NOTSET,
        optStructVal: _typing.Union[MyData, '__NotSet', None]=NOTSET,
        optLateStructVal: _typing.Union[LateDefStruct, '__NotSet', None]=NOTSET,
        optListVal: _typing.Union[_typing.Sequence[int], '__NotSet', None]=NOTSET,
        optSetVal: _typing.Union[_typing.AbstractSet[str], '__NotSet', None]=NOTSET,
        optMapVal: _typing.Union[_typing.Mapping[str, str], '__NotSet', None]=NOTSET,
        listMap: _typing.Union[_typing.Sequence[_typing.Mapping[str, int]], '__NotSet', None]=NOTSET,
        mapMap: _typing.Union[_typing.Mapping[str, _typing.Mapping[str, int]], '__NotSet', None]=NOTSET
    ) -> MyStruct: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['MyStruct'], bytes]]: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'MyStruct') -> bool: ...
    def __gt__(self, other: 'MyStruct') -> bool: ...
    def __le__(self, other: 'MyStruct') -> bool: ...
    def __ge__(self, other: 'MyStruct') -> bool: ...

    def _to_python(self) -> "test.fixtures.patch.module.thrift_types.MyStruct": ...   # type: ignore
    def _to_py3(self) -> MyStruct: ...
    def _to_py_deprecated(self) -> "module.ttypes.MyStruct": ...   # type: ignore

class LateDefStruct(thrift.py3.types.Struct, _typing.Hashable):
    class __fbthrift_IsSet:
        pass

    def __init__(
        self, 
    ) -> None: ...

    def __call__(
        self, 
    ) -> LateDefStruct: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['LateDefStruct'], bytes]]: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'LateDefStruct') -> bool: ...
    def __gt__(self, other: 'LateDefStruct') -> bool: ...
    def __le__(self, other: 'LateDefStruct') -> bool: ...
    def __ge__(self, other: 'LateDefStruct') -> bool: ...

    def _to_python(self) -> "test.fixtures.patch.module.thrift_types.LateDefStruct": ...   # type: ignore
    def _to_py3(self) -> LateDefStruct: ...
    def _to_py_deprecated(self) -> "module.ttypes.LateDefStruct": ...   # type: ignore

class Recursive(thrift.py3.types.Struct, _typing.Hashable):
    class __fbthrift_IsSet:
        pass

    nodes: Final[_typing.Mapping[str, Recursive]] = ...

    def __init__(
        self, *,
        nodes: _typing.Optional[_typing.Mapping[str, Recursive]]=None
    ) -> None: ...

    def __call__(
        self, *,
        nodes: _typing.Union[_typing.Mapping[str, Recursive], '__NotSet', None]=NOTSET
    ) -> Recursive: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['Recursive'], bytes]]: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'Recursive') -> bool: ...
    def __gt__(self, other: 'Recursive') -> bool: ...
    def __le__(self, other: 'Recursive') -> bool: ...
    def __ge__(self, other: 'Recursive') -> bool: ...

    def _to_python(self) -> "test.fixtures.patch.module.thrift_types.Recursive": ...   # type: ignore
    def _to_py3(self) -> Recursive: ...
    def _to_py_deprecated(self) -> "module.ttypes.Recursive": ...   # type: ignore

class Bar(thrift.py3.types.Struct, _typing.Hashable):
    class __fbthrift_IsSet:
        pass

    loop: Final[_typing.Optional[Loop]] = ...

    def __init__(
        self, *,
        loop: _typing.Optional[Loop]=None
    ) -> None: ...

    def __call__(
        self, *,
        loop: _typing.Union[Loop, '__NotSet', None]=NOTSET
    ) -> Bar: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['Bar'], bytes]]: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'Bar') -> bool: ...
    def __gt__(self, other: 'Bar') -> bool: ...
    def __le__(self, other: 'Bar') -> bool: ...
    def __ge__(self, other: 'Bar') -> bool: ...

    def _to_python(self) -> "test.fixtures.patch.module.thrift_types.Bar": ...   # type: ignore
    def _to_py3(self) -> Bar: ...
    def _to_py_deprecated(self) -> "module.ttypes.Bar": ...   # type: ignore

class Loop(thrift.py3.types.Struct, _typing.Hashable):
    class __fbthrift_IsSet:
        pass

    bar: Final[Bar] = ...

    def __init__(
        self, *,
        bar: _typing.Optional[Bar]=None
    ) -> None: ...

    def __call__(
        self, *,
        bar: _typing.Union[Bar, '__NotSet', None]=NOTSET
    ) -> Loop: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['Loop'], bytes]]: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'Loop') -> bool: ...
    def __gt__(self, other: 'Loop') -> bool: ...
    def __le__(self, other: 'Loop') -> bool: ...
    def __ge__(self, other: 'Loop') -> bool: ...

    def _to_python(self) -> "test.fixtures.patch.module.thrift_types.Loop": ...   # type: ignore
    def _to_py3(self) -> Loop: ...
    def _to_py_deprecated(self) -> "module.ttypes.Loop": ...   # type: ignore

_List__i16T = _typing.TypeVar('_List__i16T', bound=_typing.Sequence[int])


class List__i16(_typing.Sequence[int], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.Sequence[int]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.Sequence[int]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> int: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[int]: ...
    def __add__(self, other: _typing.Sequence[int]) -> 'List__i16': ...
    def __radd__(self, other: _List__i16T) -> _List__i16T: ...
    def __reversed__(self) -> _typing.Iterator[int]: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


class Set__string(_typing.AbstractSet[str], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.AbstractSet[str]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.AbstractSet[str]: ...
    def __contains__(self, x: object) -> bool: ...
    def union(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def intersection(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def difference(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def symmetric_difference(self, other: _typing.AbstractSet[str]) -> 'Set__string': ...
    def issubset(self, other: _typing.AbstractSet[str]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[str]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


class Map__string_string(_typing.Mapping[str, str], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.Mapping[str, str]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.Mapping[str, str]: ...
    def __getitem__(self, key: str) -> str: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


class Map__string_i32(_typing.Mapping[str, int], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.Mapping[str, int]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.Mapping[str, int]: ...
    def __getitem__(self, key: str) -> int: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


_List__Map__string_i32T = _typing.TypeVar('_List__Map__string_i32T', bound=_typing.Sequence[_typing.Mapping[str, int]])


class List__Map__string_i32(_typing.Sequence[_typing.Mapping[str, int]], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.Sequence[_typing.Mapping[str, int]]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.Sequence[_typing.Mapping[str, int]]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> _typing.Mapping[str, int]: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[_typing.Mapping[str, int]]: ...
    def __add__(self, other: _typing.Sequence[_typing.Mapping[str, int]]) -> 'List__Map__string_i32': ...
    def __radd__(self, other: _List__Map__string_i32T) -> _List__Map__string_i32T: ...
    def __reversed__(self) -> _typing.Iterator[_typing.Mapping[str, int]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Mapping[str, int]]: ...


class Map__string_Map__string_i32(_typing.Mapping[str, _typing.Mapping[str, int]], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.Mapping[str, _typing.Mapping[str, int]]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.Mapping[str, _typing.Mapping[str, int]]: ...
    def __getitem__(self, key: str) -> _typing.Mapping[str, int]: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


class Map__string_Recursive(_typing.Mapping[str, Recursive], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.Mapping[str, Recursive]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.Mapping[str, Recursive]: ...
    def __getitem__(self, key: str) -> Recursive: ...
    def __iter__(self) -> _typing.Iterator[str]: ...


