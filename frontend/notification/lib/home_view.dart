import 'package:flutter/material.dart';

import 'intro_view.dart';

class HomeView extends StatelessWidget {
  const HomeView({Key? key}) : super(key: key);

  Widget _drawerOption(String text) {
    return Text(text, style: const TextStyle(fontSize: 16.0));
  }

  Widget _mainButtonFragment(BuildContext context) {
    return SizedBox(
      height: 70.0,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          ElevatedButton(
            child: const Text('Diary'),
            onPressed: () {
              Navigator.pushNamed(context, '/dashboard',
                  arguments: 'diary');
            },
          ),
          ElevatedButton(
            child: const Text('Task'),
            onPressed: () {
              Navigator.pushNamed(context, '/dashboard',
                  arguments: 'task');
            },
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: const Text("Home")),
        drawer: Drawer(
            child: ListView(
          children: [
            const UserAccountsDrawerHeader(
              currentAccountPicture: CircleAvatar(
                child: Icon(Icons.person),
              ),
              accountName: Text("User Name"),
              accountEmail: Text("notification.app@email.com"),
            ),
            ListTile(
              leading: const Icon(Icons.check),
              title: _drawerOption("Authentication"),
              onTap: () {},
            ),
            ListTile(
              leading: const Icon(Icons.settings),
              title: _drawerOption("Setting"),
              onTap: () {},
            ),
          ],
        )),
        body: Stack(
          children: [
            const IntroView(),
            Center(child: _mainButtonFragment(context)),
          ],
        ));
  }
}
