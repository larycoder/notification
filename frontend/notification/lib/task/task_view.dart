import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:notification/constant/type.dart';
import 'package:notification/models/task_model.dart';

import 'note_fragment.dart';

/// Detail view of task
class TaskView extends StatelessWidget {
  final int localId;
  final TaskModel data;

  const TaskView(this.data, this.localId, {Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text(data.task!)),
        body: Column(
          children: [
            NoteFragment(data),
            TextButton(
                child: const Text("Save"),
                onPressed: () {
                  Hive.box(DataType.task).put(localId, data);
                  Navigator.pop(context);
                }),
          ],
        ));
  }

  /// Clone new task view from current one
  TaskView clone() {
    return TaskView(data, localId);
  }
}
