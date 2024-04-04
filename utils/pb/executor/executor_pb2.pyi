from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutorRequest(_message.Message):
    __slots__ = ("input", "id", "len_data")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEN_DATA_FIELD_NUMBER: _ClassVar[int]
    input: str
    id: str
    len_data: int
    def __init__(self, input: _Optional[str] = ..., id: _Optional[str] = ..., len_data: _Optional[int] = ...) -> None: ...

class ExecutorResponse(_message.Message):
    __slots__ = ("status", "id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    status: str
    id: str
    def __init__(self, status: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
