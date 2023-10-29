import 'package:flutter/material.dart';

class MyListView extends StatelessWidget {
  List<Widget> tambahItem(int count) {
    List<Widget> items = [];
    for (var i = 0; i < count; i++) {
      items.add(ListTile(
        title: Text("Item ${i + 1}"),
        leading: Icon(Icons.person),
        trailing: Icon(Icons.delete),
      ));
      items.add(Divider(
        color: Colors.blue,
      ));
    }
    return items; // You need to return the list of items
  }

  MyListView({Key? key}) : super(key: key); // Provide a key to the constructor

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("List View dengan LOOP"),
      ),
      body: ListView(
        padding: EdgeInsets.all(20.0),
        children: tambahItem(30),
      ),
    );
  }
}
