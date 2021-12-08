import 'package:flutter/material.dart';

class DashboardView extends StatefulWidget {
  const DashboardView({Key? key}) : super(key: key);

  @override
  State<DashboardView> createState() => _DashboardViewState();
}

class _DashboardViewState extends State<DashboardView> {
  String noteType = "diary";

  Widget _noteListFragment(BuildContext context) {
    final items =
        List<String>.generate(100, (i) => "item $i"); // for debug only
    return ListView.builder(
      itemCount: items.length,
      itemBuilder: (context, index) {
        return ListTile(title: Text(items[index]));
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    noteType = ModalRoute.of(context)!.settings.arguments as String;
    return Scaffold(
      appBar: AppBar(title: Text("Dashboard $noteType")),
      body: _noteListFragment(context),
    );
  }
}
