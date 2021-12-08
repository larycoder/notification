import 'package:flutter/material.dart';
import 'package:hive_flutter/hive_flutter.dart';

import 'home_view.dart';
import 'pages/note/dashboard_view.dart';

void main() async {
  await Hive.initFlutter();
  runApp(
    MaterialApp(
      title: 'Notification App',
      theme: ThemeData(primarySwatch: Colors.blue),
      initialRoute: '/',
      routes: {
        '/': (context) => const HomeView(),
        '/dashboard': (context) => const DashboardView(),
      },
    ),
  );
}
