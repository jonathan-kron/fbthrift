/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#include <thrift/lib/cpp2/gen/module_metadata_cpp.h>
#include "thrift/compiler/test/fixtures/frozen-struct/gen-cpp2/module_metadata.h"

namespace apache {
namespace thrift {
namespace detail {
namespace md {
using ThriftMetadata = ::apache::thrift::metadata::ThriftMetadata;
using ThriftPrimitiveType = ::apache::thrift::metadata::ThriftPrimitiveType;
using ThriftType = ::apache::thrift::metadata::ThriftType;

void EnumMetadata<::some::ns::EnumB>::gen(ThriftMetadata& metadata) {
  auto res = metadata.enums.emplace("module.EnumB", ::apache::thrift::metadata::ThriftEnum{});
  if (!res.second) {
    return;
  }
  ::apache::thrift::metadata::ThriftEnum& enum_metadata = res.first->second;
  enum_metadata.name = "module.EnumB";
  for (const auto& p : ::some::ns::_EnumB_VALUES_TO_NAMES) {
    enum_metadata.elements.emplace(static_cast<int32_t>(p.first), p.second) ;
  }
}

void StructMetadata<::some::ns::ModuleA>::gen(ThriftMetadata& metadata) {
  auto res = metadata.structs.emplace("module.ModuleA", ::apache::thrift::metadata::ThriftStruct{});
  if (!res.second) {
    return;
  }
  ::apache::thrift::metadata::ThriftStruct& module_ModuleA = res.first->second;
  module_ModuleA.name = "module.ModuleA";
  module_ModuleA.is_union = false;
  static const std::tuple<int32_t, const char*, bool, std::unique_ptr<MetadataTypeInterface>>
  module_ModuleA_fields[] = {
    {1, "i32Field", false, std::make_unique<Primitive>(ThriftPrimitiveType::I32)},
    {2, "strField", false, std::make_unique<Primitive>(ThriftPrimitiveType::STRING)},
    {3, "listField", false, std::make_unique<List>(std::make_unique<Primitive>(ThriftPrimitiveType::I16))},
    {4, "mapField", false, std::make_unique<Map>(std::make_unique<Primitive>(ThriftPrimitiveType::STRING), std::make_unique<Primitive>(ThriftPrimitiveType::I32))},
    {5, "inclAField", false, std::make_unique<Struct< ::some::ns::IncludedA>>("include1.IncludedA", metadata)},
    {6, "inclBField", false, std::make_unique<Struct< ::some::ns::IncludedB>>("include2.IncludedB", metadata)},
  };
  for (const auto& f : module_ModuleA_fields) {
    ::apache::thrift::metadata::ThriftField field;
    field.id = std::get<0>(f);
    field.name = std::get<1>(f);
    field.is_optional = std::get<2>(f);
    std::get<3>(f)->initialize(field.type);
    module_ModuleA.fields.push_back(std::move(field));
  }
}
void StructMetadata<::some::ns::ModuleB>::gen(ThriftMetadata& metadata) {
  auto res = metadata.structs.emplace("module.ModuleB", ::apache::thrift::metadata::ThriftStruct{});
  if (!res.second) {
    return;
  }
  ::apache::thrift::metadata::ThriftStruct& module_ModuleB = res.first->second;
  module_ModuleB.name = "module.ModuleB";
  module_ModuleB.is_union = false;
  static const std::tuple<int32_t, const char*, bool, std::unique_ptr<MetadataTypeInterface>>
  module_ModuleB_fields[] = {
    {1, "i32Field", false, std::make_unique<Primitive>(ThriftPrimitiveType::I32)},
    {2, "inclEnumB", false, std::make_unique<Enum< ::some::ns::EnumB>>("module.EnumB", metadata)},
  };
  for (const auto& f : module_ModuleB_fields) {
    ::apache::thrift::metadata::ThriftField field;
    field.id = std::get<0>(f);
    field.name = std::get<1>(f);
    field.is_optional = std::get<2>(f);
    std::get<3>(f)->initialize(field.type);
    module_ModuleB.fields.push_back(std::move(field));
  }
}

} // namespace md
} // namespace detail
} // namespace thrift
} // namespace apache
