import 'package:flutter/material.dart';

class DrawerView extends StatelessWidget {
  const DrawerView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Drawer(
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
          title: const Text("Authentication", style: TextStyle(fontSize: 16.0)),
          onTap: () {},
        ),
        ListTile(
          leading: const Icon(Icons.settings),
          title: const Text("Authentication", style: TextStyle(fontSize: 16.0)),
          onTap: () {},
        ),
      ],
    ));
  }
}
