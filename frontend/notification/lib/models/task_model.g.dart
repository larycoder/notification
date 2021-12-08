// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'task_model.dart';

// **************************************************************************
// TypeAdapterGenerator
// **************************************************************************

class TaskModelAdapter extends TypeAdapter<TaskModel> {
  @override
  final int typeId = 0;

  @override
  TaskModel read(BinaryReader reader) {
    final numOfFields = reader.readByte();
    final fields = <int, dynamic>{
      for (int i = 0; i < numOfFields; i++) reader.readByte(): reader.read(),
    };
    return TaskModel(
      id: fields[0] as int?,
      parentId: fields[1] as int?,
      task: fields[2] as String?,
      notes: fields[3] as String?,
      label: fields[4] as String?,
      priority: fields[5] as String?,
      created_time: fields[6] as DateTime?,
      deadline: fields[7] as DateTime?,
      measurement: fields[8] as String?,
      process: fields[9] as String?,
    );
  }

  @override
  void write(BinaryWriter writer, TaskModel obj) {
    writer
      ..writeByte(10)
      ..writeByte(0)
      ..write(obj.id)
      ..writeByte(1)
      ..write(obj.parentId)
      ..writeByte(2)
      ..write(obj.task)
      ..writeByte(3)
      ..write(obj.notes)
      ..writeByte(4)
      ..write(obj.label)
      ..writeByte(5)
      ..write(obj.priority)
      ..writeByte(6)
      ..write(obj.created_time)
      ..writeByte(7)
      ..write(obj.deadline)
      ..writeByte(8)
      ..write(obj.measurement)
      ..writeByte(9)
      ..write(obj.process);
  }

  @override
  int get hashCode => typeId.hashCode;

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is TaskModelAdapter &&
          runtimeType == other.runtimeType &&
          typeId == other.typeId;
}
