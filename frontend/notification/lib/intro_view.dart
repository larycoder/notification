import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_markdown/flutter_markdown.dart';

class IntroView extends StatefulWidget {
  const IntroView({Key? key}) : super(key: key);

  @override
  State<IntroView> createState() => _IntroViewState();
}

class _IntroViewState extends State<IntroView> {
  Future<Widget> _presentMarkdown() async {
    String text = await rootBundle.loadString("lib/asserts/introduction.txt");
    return Markdown(data: text);
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<Widget>(
        future: _presentMarkdown(),
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return snapshot.data!;
          } else if (snapshot.hasError) {
            return const Text("could not load intro");
          } else {
            return const CircularProgressIndicator();
          }
        });
  }
}
