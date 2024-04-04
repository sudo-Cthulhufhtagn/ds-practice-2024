from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SuggestionRequest(_message.Message):
    __slots__ = ("input", "id", "clock")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    input: str
    id: str
    clock: str
    def __init__(self, input: _Optional[str] = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...

class SuggestionResponse(_message.Message):
    __slots__ = ("suggestion", "id", "clock")
    SUGGESTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CLOCK_FIELD_NUMBER: _ClassVar[int]
    suggestion: str
    id: str
    clock: str
    def __init__(self, suggestion: _Optional[str] = ..., id: _Optional[str] = ..., clock: _Optional[str] = ...) -> None: ...
