// ignore_for_file: non_constant_identifier_names

import 'package:hive/hive.dart';

part 'task_model.g.dart';

@HiveType(typeId: 0)
class TaskModel {
  @HiveField(0)
  int? id;

  @HiveField(1)
  int? parentId;

  @HiveField(2)
  String? task;

  @HiveField(3)
  String? notes;

  @HiveField(4)
  String? label;

  @HiveField(5)
  String? priority;

  @HiveField(6)
  DateTime? created_time;

  @HiveField(7)
  DateTime? deadline;

  @HiveField(8)
  String? measurement;

  @HiveField(9)
  double? process;

  TaskModel({
    this.id,
    this.parentId,
    this.task,
    this.notes,
    this.label,
    this.priority,
    this.created_time,
    this.deadline,
    this.measurement,
    this.process,
  });
}
