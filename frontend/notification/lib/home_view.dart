import 'package:flutter/material.dart';

import 'dashboard/dashboard_view.dart';
import 'drawer_view.dart';

class HomeView extends StatelessWidget {
  const HomeView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Home")),
      drawer: const DrawerView(),
      body: const DashboardView(),
    );
  }
}
