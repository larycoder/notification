import 'package:flutter/material.dart';
import 'package:notification/models/diary_model.dart';
import 'package:notification/models/task_model.dart';

/// A custom class used to fast build the note view
///
/// NoteView is the abstract class wraps around ListTile class with extra
/// decoration helping to build a consistent design of single note for both
/// diary and task note.
///
/// ## Implementation
/// The abstract class has already defined build method, hence, the concrete
/// class MUST not override this method, instead, the concrete class need to
/// override **_buildInformation** method which is used to provide data for
/// ListTile.
abstract class NoteView extends StatelessWidget {
  const NoteView({Key? key}) : super(key: key);

  /// Provide parameter for ListTile
  ///
  /// The method return a Map<String, Widget> which must contain 4 keys
  /// corresponding to 4 parameters in ListTile: leading, title, subtitle and
  /// trailing. The values will be correspond widget for those positions.
  ///
  /// Example of expected return:
  /// ```dart
  /// {
  ///   "leading": const Text("TK"),
  ///   "title": const Text("TK"),
  ///   "subtitle": const Text("TK"),
  ///   "trailing": const Text("TK"),
  /// }
  /// ```
  Map<String, Widget> _buildInformation(BuildContext context);

  Widget _listTileFragment(BuildContext context) {
    var info = _buildInformation(context);
    return ListTile(
      leading: Container(
        color: Theme.of(context).primaryColor,
        height: double.infinity,
        padding: const EdgeInsets.symmetric(horizontal: 20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [info["leading"]!],
        ),
      ),
      title: info["title"],
      subtitle: info["subtitle"],
      trailing: info["trailing"],
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

class TaskNote extends NoteView {
  final TaskModel data;
  const TaskNote({Key? key, required this.data}) : super(key: key);

  @override
  Map<String, Widget> _buildInformation(BuildContext context) {
    return {
      "leading": Text(
        data.priority?.toUpperCase() ?? "N",
        style: const TextStyle(color: Colors.white),
      ),
      "title": Text("task: ${data.task ?? ""}"),
      "subtitle": Text(
        "deadline: ${data.deadline?.toIso8601String() ?? ""}",
      ),
      "trailing": Text("${data.id ?? -1}"),
    };
  }
}

class DiaryNote extends NoteView {
  final DiaryModel data;
  const DiaryNote({Key? key, required this.data}) : super(key: key);

  @override
  Map<String, Widget> _buildInformation(BuildContext context) {
    Duration duration = Duration(seconds: data.duration ?? 0);
    return {
      "leading": Text(
        duration.toString(),
        style: const TextStyle(color: Colors.white),
      ),
      "title": Text("activity: ${data.activity ?? ""}"),
      "subtitle": Text(
        "start_time: ${data.start_time?.toIso8601String() ?? ""}",
      ),
      "trailing": Text("${data.id ?? -1}"),
    };
  }
}
