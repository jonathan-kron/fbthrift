#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from cpython.ref cimport PyObject
from libc.stdint cimport (
    int8_t as cint8_t,
    int16_t as cint16_t,
    int32_t as cint32_t,
    int64_t as cint64_t,
)
from libcpp cimport bool as cbool
from libcpp.map cimport map as cmap, pair as cpair
from libcpp.memory cimport shared_ptr, unique_ptr
from libcpp.set cimport set as cset
from libcpp.string cimport string
from libcpp.vector cimport vector

from folly cimport cFollyFuture, cFollyTry, cFollyUnit
cimport folly.iobuf as __iobuf
from thrift.py3.common cimport cRpcOptions

cimport module.types as _module_types


cdef extern from "src/gen-cpp2/MyRoot.h" namespace "::cpp2":
  cdef cppclass cMyRootAsyncClient "::cpp2::MyRootAsyncClient":
      pass

cdef extern from "<utility>" namespace "std":
  cdef unique_ptr[cMyRootClientWrapper] move(unique_ptr[cMyRootClientWrapper])

cdef extern from "src/gen-cpp2/MyNode.h" namespace "::cpp2":
  cdef cppclass cMyNodeAsyncClient "::cpp2::MyNodeAsyncClient":
      pass

cdef extern from "<utility>" namespace "std":
  cdef unique_ptr[cMyNodeClientWrapper] move(unique_ptr[cMyNodeClientWrapper])

cdef extern from "src/gen-cpp2/MyLeaf.h" namespace "::cpp2":
  cdef cppclass cMyLeafAsyncClient "::cpp2::MyLeafAsyncClient":
      pass

cdef extern from "<utility>" namespace "std":
  cdef unique_ptr[cMyLeafClientWrapper] move(unique_ptr[cMyLeafClientWrapper])

cdef extern from "thrift/lib/cpp/TProcessorEventHandler.h" namespace "::apache::thrift":
  cdef cppclass cTProcessorEventHandler "apache::thrift::TProcessorEventHandler":
    pass

cdef extern from "src/gen-py3/module/clients_wrapper.h" namespace "::cpp2":
  cdef cppclass cMyRootClientWrapper "::cpp2::MyRootClientWrapper":
    void setPersistentHeader(const string& key, const string& value)
    void addEventHandler(const shared_ptr[cTProcessorEventHandler]& handler)

    cFollyFuture[cFollyUnit] do_root(cRpcOptions, )


  cdef cppclass cMyNodeClientWrapper "::cpp2::MyNodeClientWrapper"(cMyRootClientWrapper):

    cFollyFuture[cFollyUnit] do_mid(cRpcOptions, )


  cdef cppclass cMyLeafClientWrapper "::cpp2::MyLeafClientWrapper"(cMyNodeClientWrapper):

    cFollyFuture[cFollyUnit] do_leaf(cRpcOptions, )

