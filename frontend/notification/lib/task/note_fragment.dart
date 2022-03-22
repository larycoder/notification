import 'package:flutter/material.dart';
import 'package:notification/models/task_model.dart';

/// Present text note area
class NoteFragment extends StatefulWidget {
  final TaskModel model;
  const NoteFragment(this.model, {Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() => _NoteFragmentState();
}

class _NoteFragmentState extends State<NoteFragment> {
  final TextEditingController controller = TextEditingController();

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }

  Widget textFieldFragment(BuildContext context) {
    // initial text
    if (widget.model.notes == null) {
      controller.text = "";
    } else {
      controller.text = widget.model.notes!;
    }

    // build widget
    return TextField(
      controller: controller,
      decoration: const InputDecoration(border: InputBorder.none),
      onChanged: (String value) {
        widget.model.notes = value;
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    // set screen width and height
    double h = MediaQuery.of(context).size.height;
    double w = MediaQuery.of(context).size.width;

    // build note container
    return SizedBox(
      height: (3 / 4) * h,
      width: (3 / 4) * w,
      child: Card(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: textFieldFragment(context),
        ),
      ),
    );
  }
}
