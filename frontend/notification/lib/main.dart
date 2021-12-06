import 'package:flutter/material.dart';

import 'home_view.dart';

void main() {
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
