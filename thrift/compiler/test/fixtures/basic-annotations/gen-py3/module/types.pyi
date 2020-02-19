#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import folly.iobuf as __iobuf
import thrift.py3.types
import thrift.py3.exceptions
from thrift.py3.types import NOTSET, NOTSETTYPE
import typing as _typing
from typing_extensions import Final

import sys
import itertools


__property__ = property


class MyEnum(thrift.py3.types.Enum):
    MyValue1: MyEnum = ...
    MyValue2: MyEnum = ...
    DOMAIN: MyEnum = ...


class MyStruct(thrift.py3.types.Struct, _typing.Hashable, _typing.Iterable[_typing.Tuple[str, _typing.Any]]):
    major: Final[int] = ...

    package: Final[str] = ...

    annotation_with_quote: Final[str] = ...

    class_: Final[str] = ...

    def __init__(
        self, *,
        major: _typing.Optional[int]=None,
        package: _typing.Optional[str]=None,
        annotation_with_quote: _typing.Optional[str]=None,
        class_: _typing.Optional[str]=None
    ) -> None: ...

    def __call__(
        self, *,
        major: _typing.Union[int, NOTSETTYPE, None]=NOTSET,
        package: _typing.Union[str, NOTSETTYPE, None]=NOTSET,
        annotation_with_quote: _typing.Union[str, NOTSETTYPE, None]=NOTSET,
        class_: _typing.Union[str, NOTSETTYPE, None]=NOTSET
    ) -> MyStruct: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['MyStruct'], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'MyStruct') -> bool: ...
    def __gt__(self, other: 'MyStruct') -> bool: ...
    def __le__(self, other: 'MyStruct') -> bool: ...
    def __ge__(self, other: 'MyStruct') -> bool: ...


