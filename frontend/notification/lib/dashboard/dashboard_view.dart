import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:notification/constant/type.dart';

import 'task_view.dart';

class DashboardView extends StatefulWidget {
  const DashboardView({Key? key}) : super(key: key);

  @override
  State<DashboardView> createState() => _DashboardViewState();
}

class _DashboardViewState extends State<DashboardView> {

  @override
  Widget build(BuildContext context) {
    var tasks = Hive.box(DataType.task);

    return Column(children: <Widget>[
      Row(children: <Widget>[
        TextButton(
          child: const Text("Add"),
          onPressed: () async {
            await Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const TaskCreator()),
            );
            setState((){});
          },
        ),
      ]),
      Expanded(
          child: ListView.builder(
        itemCount: tasks.length,
        itemBuilder: (context, index) {
          return TaskCard(tasks.get(index), index);
        },
      )),
    ]);
  }
}
