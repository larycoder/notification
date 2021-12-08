// ignore_for_file: non_constant_identifier_names

import 'package:hive/hive.dart';

part 'diary_model.g.dart';

@HiveType(typeId: 1)
class DiaryModel {
  @HiveField(0)
  int? id;

  @HiveField(1)
  String? activity;

  @HiveField(2)
  String? notes;

  @HiveField(3)
  DateTime? created_time;

  @HiveField(4)
  DateTime? start_time;

  @HiveField(5)
  int? duration;

  @HiveField(6)
  int? taskId;

  DiaryModel({
    this.id,
    this.activity,
    this.notes,
    this.created_time,
    this.start_time,
    this.duration,
    this.taskId,
  });
}
