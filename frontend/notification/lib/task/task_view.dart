import 'package:flutter/material.dart';
import 'package:notification/models/task_model.dart';

/// Detail view of task
class TaskView extends StatelessWidget {
  final int localId;
  final TaskModel data;

  const TaskView(this.data, this.localId, {Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(data.task!)),
      body: Text("localId: $localId"),
    );
  }

  /// Clone new task view from current one
  TaskView clone() {
    return TaskView(data, localId);
  }
}
