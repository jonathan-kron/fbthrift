from cython.operator cimport dereference as deref
from enum import Enum, Flag


class TransportErrorType(Enum):
    UNKNOWN = cTTransportExceptionType__UNKNOWN
    NOT_OPEN = cTTransportExceptionType__NOT_OPEN
    ALREADY_OPEN = cTTransportExceptionType__ALREADY_OPEN
    TIMED_OUT = cTTransportExceptionType__TIMED_OUT
    END_OF_FILE = cTTransportExceptionType__END_OF_FILE
    INTERRUPTED = cTTransportExceptionType__INTERRUPTED
    BAD_ARGS = cTTransportExceptionType__BAD_ARGS
    CORRUPTED_DATA = cTTransportExceptionType__CORRUPTED_DATA
    INTERNAL_ERROR = cTTransportExceptionType__INTERNAL_ERROR
    NOT_SUPPORTED = cTTransportExceptionType__NOT_SUPPORTED
    INVALID_STATE = cTTransportExceptionType__INVALID_STATE
    INVALID_FRAME_SIZE = cTTransportExceptionType__INVALID_FRAME_SIZE
    SSL_ERROR = cTTransportExceptionType__SSL_ERROR
    COULD_NOT_BIND = cTTransportExceptionType__COULD_NOT_BIND
    SASL_HANDSHAKE_TIMEOUT = cTTransportExceptionType__SASL_HANDSHAKE_TIMEOUT
    NETWORK_ERROR = cTTransportExceptionType__NETWORK_ERROR


class TransportOptions(Flag):
    CHANNEL_IS_VALID = cTTransportExceptionOptions__CHANNEL_IS_VALID


class ApplicationErrorType(Enum):
    UNKNOWN = cTApplicationExceptionType__UNKNOWN
    UNKNOWN_METHOD = cTApplicationExceptionType__UNKNOWN_METHOD
    INVALID_MESSAGE_TYPE = cTApplicationExceptionType__INVALID_MESSAGE_TYPE
    WRONG_METHOD_NAME = cTApplicationExceptionType__WRONG_METHOD_NAME
    BAD_SEQUENCE_ID = cTApplicationExceptionType__BAD_SEQUENCE_ID
    MISSING_RESULT = cTApplicationExceptionType__MISSING_RESULT
    INTERNAL_ERROR = cTApplicationExceptionType__INTERNAL_ERROR
    PROTOCOL_ERROR = cTApplicationExceptionType__PROTOCOL_ERROR
    INVALID_TRANSFORM = cTApplicationExceptionType__INVALID_TRANSFORM
    INVALID_PROTOCOL = cTApplicationExceptionType__INVALID_PROTOCOL
    UNSUPPORTED_CLIENT_TYPE = cTApplicationExceptionType__UNSUPPORTED_CLIENT_TYPE
    LOADSHEDDING = cTApplicationExceptionType__LOADSHEDDING
    TIMEOUT = cTApplicationExceptionType__TIMEOUT
    INJECTED_FAILURE = cTApplicationExceptionType__INJECTED_FAILURE


cdef class Error(Exception):
    """base class for all thrift exceptions (TException)"""
    def __init__(self, *args):
        raise TypeError('Instancing Error from Python')


cdef create_Error(shared_ptr[cTException] ex):
    if not ex:
        return
    message = (<bytes>deref(ex).what()).decode('utf-8')
    inst = <Error>Error.__new__(Error, message)
    return inst


cdef class ApplicationError(Error):
    """All Application Level Errors (TApplicationException)"""

    def __init__(ApplicationError self, type, str message):
        assert type in ApplicationErrorType, f"{type} not in ApplicationErrorType"
        assert message, "message is empty"

    @property
    def type(self):
        return self.args[0]

    @property
    def message(self):
        return self.args[1]


cdef create_ApplicationError(shared_ptr[cTApplicationException] ex):
    if not ex:
        return
    type = ApplicationErrorType(deref(ex).getType())
    message = (<bytes>deref(ex).what()).decode('utf-8')
    # Strip out the message prefix its verbose for python
    message = message[message.startswith('TApplicationException: ')*23:]
    inst = <ApplicationError>ApplicationError.__new__(
        ApplicationError,
        type,
        message,
    )
    return inst


cdef class LibraryError(Error):
    """Equivalent of a C++ TLibraryException"""
    def __init__(self, *args):
        raise TypeError('Instancing LibraryError from Python')


cdef create_LibraryError(shared_ptr[cTLibraryException] ex):
    if not ex:
        return
    message = (<bytes>deref(ex).what()).decode('utf-8')
    inst = <LibraryError>LibraryError.__new__(LibraryError, message)
    return inst


cdef class TransportError(LibraryError):
    """All Transport Level Errors (TTransportException)"""

    def __init__(self, *args):
        raise TypeError('Instancing TransportError from Python')

    @property
    def type(self):
        return self.args[0]

    @property
    def message(self):
        return self.args[1]

    @property
    def errno(self):
        return self.args[2]

    @property
    def options(self):
        return self.args[3]


cdef create_TransportError(shared_ptr[cTTransportException] ex):
    if not ex:
        return
    type = TransportErrorType(deref(ex).getType())
    options = TransportOptions(deref(ex).getOptions())
    Errno = deref(ex).getErrno()
    message = (<bytes>deref(ex).what()).decode('utf-8')
    # Strip off the c++ message prefix
    message = message[message.startswith('TTransportException: ')*21:]
    inst = <TransportError>TransportError.__new__(
        TransportError,
        type,
        message,
        Errno,
        options,
    )
    return inst


cdef raise_py_exception(const cFollyExceptionWrapper& ex):
    # This will raise an exception if a handler raised one
    runHandlers(ex)

    pyex = create_ApplicationError(try_make_shared_exception[cTApplicationException](ex))
    if pyex:
        raise pyex

    pyex = create_TransportError(try_make_shared_exception[cTTransportException](ex))
    if pyex:
        raise pyex

    pyex = create_LibraryError(try_make_shared_exception[cTLibraryException](ex))
    if pyex:
        raise pyex

    pyex = create_Error(try_make_shared_exception[cTException](ex))
    if pyex:
        raise pyex

    # No clue what this is just throw it and let the default cython logic takeover
    ex.throw_exception()
