from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NameRequest(_message.Message):
    __slots__ = ("name", "id", "clock")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    clock: str
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...

class ExpRequest(_message.Message):
    __slots__ = ("ExpDate", "id", "clock")
    EXPDATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    ExpDate: str
    id: str
    clock: str
    def __init__(self, ExpDate: _Optional[str] = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...

class NameResponse(_message.Message):
    __slots__ = ("status2", "id", "clock")
    STATUS2_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    status2: bool
    id: str
    clock: str
    def __init__(self, status2: bool = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...

class ExpResponse(_message.Message):
    __slots__ = ("status", "id", "clock")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    status: bool
    id: str
    clock: str
    def __init__(self, status: bool = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ("greeting",)
    GREETING_FIELD_NUMBER: _ClassVar[int]
    greeting: str
    def __init__(self, greeting: _Optional[str] = ...) -> None: ...
