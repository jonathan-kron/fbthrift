/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

package test.fixtures.patch;

import com.facebook.swift.codec.*;
import com.facebook.swift.codec.ThriftField.Requiredness;
import com.facebook.swift.codec.ThriftField.Recursiveness;
import com.google.common.collect.*;
import java.util.*;
import javax.annotation.Nullable;
import org.apache.thrift.*;
import org.apache.thrift.transport.*;
import org.apache.thrift.protocol.*;
import static com.google.common.base.MoreObjects.toStringHelper;
import static com.google.common.base.MoreObjects.ToStringHelper;

@SwiftGenerated
@com.facebook.swift.codec.ThriftStruct(value="MyStructField27Patch", builder=MyStructField27Patch.Builder.class)
public final class MyStructField27Patch implements com.facebook.thrift.payload.ThriftSerializable {

    @ThriftConstructor
    public MyStructField27Patch(
        @com.facebook.swift.codec.ThriftField(value=1, name="assign", requiredness=Requiredness.OPTIONAL) final List<Short> assign,
        @com.facebook.swift.codec.ThriftField(value=2, name="clear", requiredness=Requiredness.NONE) final boolean clear,
        @com.facebook.swift.codec.ThriftField(value=3, name="patch", requiredness=Requiredness.NONE) final Map<Integer, com.facebook.thrift.op.I16Patch> patch,
        @com.facebook.swift.codec.ThriftField(value=7, name="remove", requiredness=Requiredness.NONE) final List<Short> remove,
        @com.facebook.swift.codec.ThriftField(value=8, name="prepend", requiredness=Requiredness.NONE) final List<Short> prepend,
        @com.facebook.swift.codec.ThriftField(value=9, name="append", requiredness=Requiredness.NONE) final List<Short> append
    ) {
        this.assign = assign;
        this.clear = clear;
        this.patch = patch;
        this.remove = remove;
        this.prepend = prepend;
        this.append = append;
    }
    
    @ThriftConstructor
    protected MyStructField27Patch() {
      this.assign = null;
      this.clear = false;
      this.patch = null;
      this.remove = null;
      this.prepend = null;
      this.append = null;
    }
    
    public static class Builder {
    
        private List<Short> assign = null;
        private boolean clear = false;
        private Map<Integer, com.facebook.thrift.op.I16Patch> patch = null;
        private List<Short> remove = null;
        private List<Short> prepend = null;
        private List<Short> append = null;
    
        @com.facebook.swift.codec.ThriftField(value=1, name="assign", requiredness=Requiredness.OPTIONAL)
        public Builder setAssign(List<Short> assign) {
            this.assign = assign;
            return this;
        }
    
        public List<Short> getAssign() { return assign; }
    
            @com.facebook.swift.codec.ThriftField(value=2, name="clear", requiredness=Requiredness.NONE)
        public Builder setClear(boolean clear) {
            this.clear = clear;
            return this;
        }
    
        public boolean isClear() { return clear; }
    
            @com.facebook.swift.codec.ThriftField(value=3, name="patch", requiredness=Requiredness.NONE)
        public Builder setPatch(Map<Integer, com.facebook.thrift.op.I16Patch> patch) {
            this.patch = patch;
            return this;
        }
    
        public Map<Integer, com.facebook.thrift.op.I16Patch> getPatch() { return patch; }
    
            @com.facebook.swift.codec.ThriftField(value=7, name="remove", requiredness=Requiredness.NONE)
        public Builder setRemove(List<Short> remove) {
            this.remove = remove;
            return this;
        }
    
        public List<Short> getRemove() { return remove; }
    
            @com.facebook.swift.codec.ThriftField(value=8, name="prepend", requiredness=Requiredness.NONE)
        public Builder setPrepend(List<Short> prepend) {
            this.prepend = prepend;
            return this;
        }
    
        public List<Short> getPrepend() { return prepend; }
    
            @com.facebook.swift.codec.ThriftField(value=9, name="append", requiredness=Requiredness.NONE)
        public Builder setAppend(List<Short> append) {
            this.append = append;
            return this;
        }
    
        public List<Short> getAppend() { return append; }
    
        public Builder() { }
        public Builder(MyStructField27Patch other) {
            this.assign = other.assign;
            this.clear = other.clear;
            this.patch = other.patch;
            this.remove = other.remove;
            this.prepend = other.prepend;
            this.append = other.append;
        }
    
        @ThriftConstructor
        public MyStructField27Patch build() {
            MyStructField27Patch result = new MyStructField27Patch (
                this.assign,
                this.clear,
                this.patch,
                this.remove,
                this.prepend,
                this.append
            );
            return result;
        }
    }
        
    public static final Map<String, Integer> NAMES_TO_IDS = new HashMap();
    public static final Map<String, Integer> THRIFT_NAMES_TO_IDS = new HashMap();
    public static final Map<Integer, TField> FIELD_METADATA = new HashMap<>();
    private static final TStruct STRUCT_DESC = new TStruct("MyStructField27Patch");
    private final List<Short> assign;
    public static final int _ASSIGN = 1;
    private static final TField ASSIGN_FIELD_DESC = new TField("assign", TType.LIST, (short)1);
        private final boolean clear;
    public static final int _CLEAR = 2;
    private static final TField CLEAR_FIELD_DESC = new TField("clear", TType.BOOL, (short)2);
        private final Map<Integer, com.facebook.thrift.op.I16Patch> patch;
    public static final int _PATCH = 3;
    private static final TField PATCH_FIELD_DESC = new TField("patch", TType.MAP, (short)3);
        private final List<Short> remove;
    public static final int _REMOVE = 7;
    private static final TField REMOVE_FIELD_DESC = new TField("remove", TType.LIST, (short)7);
        private final List<Short> prepend;
    public static final int _PREPEND = 8;
    private static final TField PREPEND_FIELD_DESC = new TField("prepend", TType.LIST, (short)8);
        private final List<Short> append;
    public static final int _APPEND = 9;
    private static final TField APPEND_FIELD_DESC = new TField("append", TType.LIST, (short)9);
    static {
      NAMES_TO_IDS.put("assign", 1);
      THRIFT_NAMES_TO_IDS.put("assign", 1);
      FIELD_METADATA.put(1, ASSIGN_FIELD_DESC);
      NAMES_TO_IDS.put("clear", 2);
      THRIFT_NAMES_TO_IDS.put("clear", 2);
      FIELD_METADATA.put(2, CLEAR_FIELD_DESC);
      NAMES_TO_IDS.put("patch", 3);
      THRIFT_NAMES_TO_IDS.put("patch", 3);
      FIELD_METADATA.put(3, PATCH_FIELD_DESC);
      NAMES_TO_IDS.put("remove", 7);
      THRIFT_NAMES_TO_IDS.put("remove", 7);
      FIELD_METADATA.put(7, REMOVE_FIELD_DESC);
      NAMES_TO_IDS.put("prepend", 8);
      THRIFT_NAMES_TO_IDS.put("prepend", 8);
      FIELD_METADATA.put(8, PREPEND_FIELD_DESC);
      NAMES_TO_IDS.put("append", 9);
      THRIFT_NAMES_TO_IDS.put("append", 9);
      FIELD_METADATA.put(9, APPEND_FIELD_DESC);
      com.facebook.thrift.type.TypeRegistry.add(new com.facebook.thrift.type.Type(
        new com.facebook.thrift.type.UniversalName("test.dev/fixtures/patch/MyStructField27Patch"), 
        MyStructField27Patch.class, MyStructField27Patch::read0));
    }
    
    @Nullable
    @com.facebook.swift.codec.ThriftField(value=1, name="assign", requiredness=Requiredness.OPTIONAL)
    public List<Short> getAssign() { return assign; }
    
    
    
    @com.facebook.swift.codec.ThriftField(value=2, name="clear", requiredness=Requiredness.NONE)
    public boolean isClear() { return clear; }
    
    
    @Nullable
    @com.facebook.swift.codec.ThriftField(value=3, name="patch", requiredness=Requiredness.NONE)
    public Map<Integer, com.facebook.thrift.op.I16Patch> getPatch() { return patch; }
    
    
    @Nullable
    @com.facebook.swift.codec.ThriftField(value=7, name="remove", requiredness=Requiredness.NONE)
    public List<Short> getRemove() { return remove; }
    
    
    @Nullable
    @com.facebook.swift.codec.ThriftField(value=8, name="prepend", requiredness=Requiredness.NONE)
    public List<Short> getPrepend() { return prepend; }
    
    
    @Nullable
    @com.facebook.swift.codec.ThriftField(value=9, name="append", requiredness=Requiredness.NONE)
    public List<Short> getAppend() { return append; }
    
    @java.lang.Override
    public String toString() {
        ToStringHelper helper = toStringHelper(this);
        helper.add("assign", assign);
        helper.add("clear", clear);
        helper.add("patch", patch);
        helper.add("remove", remove);
        helper.add("prepend", prepend);
        helper.add("append", append);
        return helper.toString();
    }
    
    @java.lang.Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
    
        MyStructField27Patch other = (MyStructField27Patch)o;
    
        return
            Objects.equals(assign, other.assign) &&
            Objects.equals(clear, other.clear) &&
            Objects.equals(patch, other.patch) &&
            Objects.equals(remove, other.remove) &&
            Objects.equals(prepend, other.prepend) &&
            Objects.equals(append, other.append) &&
            true;
    }
    
    @java.lang.Override
    public int hashCode() {
        return Arrays.deepHashCode(new java.lang.Object[] {
            assign,
            clear,
            patch,
            remove,
            prepend,
            append
        });
    }
    
    
    public static com.facebook.thrift.payload.Reader<MyStructField27Patch> asReader() {
      return MyStructField27Patch::read0;
    }
    
    public static MyStructField27Patch read0(TProtocol oprot) throws TException {
      TField __field;
      oprot.readStructBegin(MyStructField27Patch.NAMES_TO_IDS, MyStructField27Patch.THRIFT_NAMES_TO_IDS, MyStructField27Patch.FIELD_METADATA);
      MyStructField27Patch.Builder builder = new MyStructField27Patch.Builder();
      while (true) {
        __field = oprot.readFieldBegin();
        if (__field.type == TType.STOP) { break; }
        switch (__field.id) {
        case _ASSIGN:
          if (__field.type == TType.LIST) {
            List<Short> assign;
            {
            TList _list = oprot.readListBegin();
            assign = new ArrayList<Short>(Math.max(0, _list.size));
            for (int _i = 0; (_list.size < 0) ? oprot.peekList() : (_i < _list.size); _i++) {
                
                short _value1 = oprot.readI16();
                assign.add(_value1);
            }
            oprot.readListEnd();
            }
            builder.setAssign(assign);
          } else {
            TProtocolUtil.skip(oprot, __field.type);
          }
          break;
        case _CLEAR:
          if (__field.type == TType.BOOL) {
            boolean clear = oprot.readBool();
            builder.setClear(clear);
          } else {
            TProtocolUtil.skip(oprot, __field.type);
          }
          break;
        case _PATCH:
          if (__field.type == TType.MAP) {
            Map<Integer, com.facebook.thrift.op.I16Patch> patch;
            {
            TMap _map = oprot.readMapBegin();
            patch = new HashMap<Integer, com.facebook.thrift.op.I16Patch>(Math.max(0, _map.size));
            for (int _i = 0; (_map.size < 0) ? oprot.peekMap() : (_i < _map.size); _i++) {
                
                int _key1 = oprot.readI32();
                com.facebook.thrift.op.I16Patch _value1 = com.facebook.thrift.op.I16Patch.read0(oprot);
                patch.put(_key1, _value1);
            }
            }
            oprot.readMapEnd();
            builder.setPatch(patch);
          } else {
            TProtocolUtil.skip(oprot, __field.type);
          }
          break;
        case _REMOVE:
          if (__field.type == TType.LIST) {
            List<Short> remove;
            {
            TList _list = oprot.readListBegin();
            remove = new ArrayList<Short>(Math.max(0, _list.size));
            for (int _i = 0; (_list.size < 0) ? oprot.peekList() : (_i < _list.size); _i++) {
                
                short _value1 = oprot.readI16();
                remove.add(_value1);
            }
            oprot.readListEnd();
            }
            builder.setRemove(remove);
          } else {
            TProtocolUtil.skip(oprot, __field.type);
          }
          break;
        case _PREPEND:
          if (__field.type == TType.LIST) {
            List<Short> prepend;
            {
            TList _list = oprot.readListBegin();
            prepend = new ArrayList<Short>(Math.max(0, _list.size));
            for (int _i = 0; (_list.size < 0) ? oprot.peekList() : (_i < _list.size); _i++) {
                
                short _value1 = oprot.readI16();
                prepend.add(_value1);
            }
            oprot.readListEnd();
            }
            builder.setPrepend(prepend);
          } else {
            TProtocolUtil.skip(oprot, __field.type);
          }
          break;
        case _APPEND:
          if (__field.type == TType.LIST) {
            List<Short> append;
            {
            TList _list = oprot.readListBegin();
            append = new ArrayList<Short>(Math.max(0, _list.size));
            for (int _i = 0; (_list.size < 0) ? oprot.peekList() : (_i < _list.size); _i++) {
                
                short _value1 = oprot.readI16();
                append.add(_value1);
            }
            oprot.readListEnd();
            }
            builder.setAppend(append);
          } else {
            TProtocolUtil.skip(oprot, __field.type);
          }
          break;
        default:
          TProtocolUtil.skip(oprot, __field.type);
          break;
        }
        oprot.readFieldEnd();
      }
      oprot.readStructEnd();
      return builder.build();
    }
    
    public void write0(TProtocol oprot) throws TException {
      oprot.writeStructBegin(STRUCT_DESC);
      if (assign != null) {
        oprot.writeFieldBegin(ASSIGN_FIELD_DESC);
        List<Short> _iter0 = assign;
        oprot.writeListBegin(new TList(TType.I16, _iter0.size()));
        for (short _iter1 : _iter0) {
          oprot.writeI16(_iter1);
        }
        oprot.writeListEnd();
        oprot.writeFieldEnd();
      }
      oprot.writeFieldBegin(CLEAR_FIELD_DESC);
      oprot.writeBool(this.clear);
      oprot.writeFieldEnd();
      if (patch != null) {
        oprot.writeFieldBegin(PATCH_FIELD_DESC);
        Map<Integer, com.facebook.thrift.op.I16Patch> _iter0 = patch;
        oprot.writeMapBegin(new TMap(TType.I32, TType.STRUCT, _iter0.size()));
        for (Map.Entry<Integer, com.facebook.thrift.op.I16Patch> _iter1 : _iter0.entrySet()) {
          oprot.writeI32(_iter1.getKey());
          _iter1.getValue().write0(oprot);
        }
        oprot.writeMapEnd();
        oprot.writeFieldEnd();
      }
      if (remove != null) {
        oprot.writeFieldBegin(REMOVE_FIELD_DESC);
        List<Short> _iter0 = remove;
        oprot.writeListBegin(new TList(TType.I16, _iter0.size()));
        for (short _iter1 : _iter0) {
          oprot.writeI16(_iter1);
        }
        oprot.writeListEnd();
        oprot.writeFieldEnd();
      }
      if (prepend != null) {
        oprot.writeFieldBegin(PREPEND_FIELD_DESC);
        List<Short> _iter0 = prepend;
        oprot.writeListBegin(new TList(TType.I16, _iter0.size()));
        for (short _iter1 : _iter0) {
          oprot.writeI16(_iter1);
        }
        oprot.writeListEnd();
        oprot.writeFieldEnd();
      }
      if (append != null) {
        oprot.writeFieldBegin(APPEND_FIELD_DESC);
        List<Short> _iter0 = append;
        oprot.writeListBegin(new TList(TType.I16, _iter0.size()));
        for (short _iter1 : _iter0) {
          oprot.writeI16(_iter1);
        }
        oprot.writeListEnd();
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }
    
    private static class _MyStructField27PatchLazy {
        private static final MyStructField27Patch _DEFAULT = new MyStructField27Patch.Builder().build();
    }
    
    public static MyStructField27Patch defaultInstance() {
        return  _MyStructField27PatchLazy._DEFAULT;
    }
}
