import 'package:flutter/material.dart';
import 'package:test/BottomNav.dart';
import 'package:test/Grid.dart';
import 'package:test/Scaffold.dart';
import 'package:test/listView.dart';
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home:MyListView()
    );
  }
}