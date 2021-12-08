import 'package:flutter/material.dart';
import 'package:hive_flutter/adapters.dart';

import 'home_view.dart';

void main() async {
  await Hive.initFlutter();
  runApp(
    MaterialApp(
      title: 'Notification App',
      theme: ThemeData(primarySwatch: Colors.blue),
      initialRoute: '/',
      routes: {
        '/': (context) => const HomeView(),
      },
    ),
  );
}
