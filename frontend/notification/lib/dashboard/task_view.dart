import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:notification/constant/type.dart';
import 'package:notification/models/task_model.dart';

/// View to add new task to storage
class TaskCreator extends StatefulWidget {
  const TaskCreator({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _TaskCreatorState();
}

class _TaskCreatorState extends State<TaskCreator> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("New task")),
      body: Form(
        key: _formKey,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Container(
              padding: const EdgeInsets.all(9),
              child: TextFormField(
                decoration: const InputDecoration(
                  hintText: "Task Title",
                  focusedBorder: OutlineInputBorder(),
                  enabledBorder: OutlineInputBorder(),
                ),
                onSaved: (msg) {
                  // save message to storage
                  TaskModel model = TaskModel()..task = msg;
                  Hive.box(DataType.task).add(model);
                },
              ),
            ),
            TextButton(
              child: const Text("Submit"),
              onPressed: () {
                _formKey.currentState!.save();
                Navigator.pop(context);
              },
            )
          ],
        ),
      ),
    );
  }
}
