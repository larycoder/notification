// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'diary_model.dart';

// **************************************************************************
// TypeAdapterGenerator
// **************************************************************************

class DiaryModelAdapter extends TypeAdapter<DiaryModel> {
  @override
  final int typeId = 1;

  @override
  DiaryModel read(BinaryReader reader) {
    final numOfFields = reader.readByte();
    final fields = <int, dynamic>{
      for (int i = 0; i < numOfFields; i++) reader.readByte(): reader.read(),
    };
    return DiaryModel(
      id: fields[0] as int?,
      activity: fields[1] as String?,
      notes: fields[2] as String?,
      created_time: fields[3] as DateTime?,
      start_time: fields[4] as DateTime?,
      duration: fields[5] as int?,
      taskId: fields[6] as int?,
    );
  }

  @override
  void write(BinaryWriter writer, DiaryModel obj) {
    writer
      ..writeByte(7)
      ..writeByte(0)
      ..write(obj.id)
      ..writeByte(1)
      ..write(obj.activity)
      ..writeByte(2)
      ..write(obj.notes)
      ..writeByte(3)
      ..write(obj.created_time)
      ..writeByte(4)
      ..write(obj.start_time)
      ..writeByte(5)
      ..write(obj.duration)
      ..writeByte(6)
      ..write(obj.taskId);
  }

  @override
  int get hashCode => typeId.hashCode;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is DiaryModelAdapter &&
          runtimeType == other.runtimeType &&
          typeId == other.typeId;
}
