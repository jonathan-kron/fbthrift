/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include <thrift/lib/cpp2/gen/module_metadata_h.h>
#include <thrift/lib/thrift/gen-cpp2/metadata_types.h>
#include <thrift/compiler/test/fixtures/basic-stack-arguments/gen-cpp2/module_types.h>

namespace apache {
namespace thrift {
namespace detail {
namespace md {
using ThriftMetadata = ::apache::thrift::metadata::ThriftMetadata;

template <>
class EnumMetadata<::cpp2::MyEnum> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::cpp2::MyStruct> {
 public:
  static void gen(ThriftMetadata& metadata);
};
} // namespace md
} // namespace detail
} // namespace thrift
} // namespace apache
