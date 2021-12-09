import 'package:flutter/material.dart';
import 'package:notification/models/task_model.dart';

class TaskNote extends StatelessWidget {
  final TaskModel data;
  const TaskNote({Key? key, required this.data}) : super(key: key);

  Widget _listTileFragment(BuildContext context) {
    return ListTile(
      leading: Text(data.task ?? "Null"),
      title: Text(data.created_time?.toIso8601String() ?? "Null"),
      subtitle: Text(data.notes ?? "Null"),
      trailing: const Text("TK"),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 8.0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(8.0),
      ),
      child: _listTileFragment(context),
    );
  }
}
