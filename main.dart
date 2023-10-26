import 'package:flutter/material.dart';
import 'package:test/columnROW.dart';
import 'package:test/latihanRK.dart';
import 'package:test/lv2.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home:RK()
    );
  }
}