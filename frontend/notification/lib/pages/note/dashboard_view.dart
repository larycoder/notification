import 'package:flutter/material.dart';
import 'package:notification/models/diary_model.dart';
import 'package:notification/models/task_model.dart';

import 'note_view.dart';

class DashboardView extends StatefulWidget {
  const DashboardView({Key? key}) : super(key: key);

  @override
  State<DashboardView> createState() => _DashboardViewState();
}

class _DashboardViewState extends State<DashboardView> {
  String? noteType;

  Widget _noteListFragment(BuildContext context) {
    // replace with repository class
    final TaskModel task = TaskModel(task: "Flutter", notes: "Test");
    final DiaryModel diary = DiaryModel(activity: "Flutter", notes: "Test");
    final items = List<NoteView>.generate(
      100,
      (i) {
        return (noteType == "diary")
            ? DiaryNote(data: diary)
            : TaskNote(data: task);
      },
    );
    return Card(
      color: Colors.grey[300],
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(15.0),
      ),
      child: ListView.builder(
        itemCount: items.length,
        itemBuilder: (context, index) {
          return ListTile(title: items[index]);
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    noteType = ModalRoute.of(context)!.settings.arguments as String? ?? "diary";
    return Scaffold(
      appBar: AppBar(title: Text("Dashboard $noteType")),
      body: _noteListFragment(context),
    );
  }
}
