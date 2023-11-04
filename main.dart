import 'package:flutter/material.dart';
import 'package:test/BottomNav.dart';
import 'package:test/ListViewVH.dart';
import 'package:test/columnROW.dart';
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: RowColumn()

    );
  }
}