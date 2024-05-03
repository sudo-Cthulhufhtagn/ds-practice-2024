from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseRead(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class DatabaseWrite(_message.Message):
    __slots__ = ("key", "data", "sender_id")
    KEY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    key: str
    data: str
    sender_id: int
    def __init__(self, key: _Optional[str] = ..., data: _Optional[str] = ..., sender_id: _Optional[int] = ...) -> None: ...

class DatabaseResponse(_message.Message):
    __slots__ = ("status", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: str
    data: str
    def __init__(self, status: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...
