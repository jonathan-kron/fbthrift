/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include <thrift/lib/cpp2/gen/module_metadata_h.h>
#include <thrift/lib/thrift/gen-cpp2/metadata_types.h>
#include <thrift/compiler/test/fixtures/fatal/gen-cpp2/module_types.h>
#include "thrift/compiler/test/fixtures/fatal/gen-cpp2/reflection_dep_B_metadata.h"
#include "thrift/compiler/test/fixtures/fatal/gen-cpp2/reflection_dep_C_metadata.h"

namespace apache {
namespace thrift {
namespace detail {
namespace md {
using ThriftMetadata = ::apache::thrift::metadata::ThriftMetadata;

template <>
class EnumMetadata<::test_cpp2::cpp_reflection::enum1> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class EnumMetadata<::test_cpp2::cpp_reflection::enum2> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class EnumMetadata<::test_cpp2::cpp_reflection::enum3> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class EnumMetadata<::test_cpp2::cpp_reflection::enum_with_special_names> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::union1> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::union2> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::union3> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::structA> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::unionA> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::structB> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::structC> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::struct1> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::struct2> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::struct3> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::struct4> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::struct5> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::struct_binary> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::dep_A_struct> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::dep_B_struct> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::annotated> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::union_with_special_names> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::struct_with_special_names> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test_cpp2::cpp_reflection::struct_with_indirections> {
 public:
  static void gen(ThriftMetadata& metadata);
};
} // namespace md
} // namespace detail
} // namespace thrift
} // namespace apache
