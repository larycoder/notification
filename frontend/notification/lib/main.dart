import 'package:flutter/material.dart';
import 'package:hive_flutter/hive_flutter.dart';

import 'constant/type.dart';
import 'home_view.dart';
import 'models/diary_model.dart';
import 'models/task_model.dart';

void main() async {

  Hive.registerAdapter(TaskModelAdapter());
  Hive.registerAdapter(DiaryModelAdapter());

  await Hive.initFlutter();
  await Hive.openBox(DataType.task);
  await Hive.openBox(DataType.diary);

  runApp(
    MaterialApp(
      title: 'Notification App',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.blue),
      initialRoute: '/',
      routes: {
        '/': (context) => const HomeView(),
      },
    ),
  );
}
