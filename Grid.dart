import 'package:flutter/material.dart';

class IniGrid extends StatelessWidget {
  const IniGrid({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("GridView"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: GridView.count(
          primary: false,
          padding: EdgeInsets.zero,
          childAspectRatio: 1.0,
          crossAxisCount: 2,
          mainAxisSpacing: 10,
          crossAxisSpacing: 10,
          children: <Widget>[
            Container(
              child: Text(
                "Container 1",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 18,
                  fontWeight: FontWeight.w700,
                ),
                textAlign: TextAlign.center,
              ),
              decoration: const BoxDecoration(
                color: Color.fromARGB(148, 85, 255, 181),
                borderRadius: BorderRadius.all(
                  Radius.circular(12.0),
                ),
              ),
            ),
            Container(
              padding: EdgeInsets.all(8),
              child: Text(
                "Container 2",
                style: TextStyle(color: Colors.black),
                textAlign: TextAlign.left,
              ),
              decoration: const BoxDecoration(
                color: Color.fromARGB(255, 85, 255, 181),
              ),
            ),
            Container(
              padding: EdgeInsets.all(8),
              child: Text(
                "Container 3",
                style: TextStyle(color: Colors.black),
                textAlign: TextAlign.left,
              ),
              decoration: const BoxDecoration(
                color: Color.fromARGB(255, 44, 188, 126),
              ),
            ),
            Container(
              padding: EdgeInsets.all(8),
              child: Text(
                "Container 4",
                style: TextStyle(color: Colors.black),
                textAlign: TextAlign.left,
              ),
              decoration: const BoxDecoration(
                color: Color.fromARGB(255, 7, 176, 103),
              ),
            ),
            Container(
              padding: EdgeInsets.all(8),
              child: Text(
                "Container 5",
                style: TextStyle(color: Colors.black),
                textAlign: TextAlign.left,
              ),
              decoration: const BoxDecoration(
                color: Color.fromARGB(255, 0, 119, 91),
              ),
            ),
            Container(
              child: Text(
                "Container 6",
                style: TextStyle(
                  color: Colors.black,
                ),
                textAlign: TextAlign.left,
              ),
              decoration: const BoxDecoration(
                color: Color.fromARGB(255, 7, 176, 103),
                borderRadius: BorderRadius.all(
                  Radius.circular(12.0),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}