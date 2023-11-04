import 'package:flutter/material.dart';

class RowColumn extends StatelessWidget {
  const RowColumn({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("ini row dan kolom"),

        ),
        body: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Container(
                height: 100,
                width: 100,
                decoration: const BoxDecoration(
                color: Colors.blue,
                ),
                ),
                Container(
                height: 100,
                width: 100,
                decoration: const BoxDecoration(
                color: Colors.blue,
                ),
                ),
                Container(
                height: 100,
                width: 100,
                decoration: const BoxDecoration(
                color: Colors.blue,
                ),
                ),
              ],
            ),
            const SizedBox(
            height: 10.0,
            ),
            Row(
              children: [
                Expanded(
                  child: Container(
                  height: 100,
                  width: 100,
                  decoration: const BoxDecoration(
                  color: Colors.blue,
                  ),
                  ),
                ),
                const SizedBox(
                width: 10.0,
                ),
                Container(
                height: 100,
                width: 100,
                decoration: const BoxDecoration(
                color: Colors.blue,
                ),
                ),
              ],
            ),
            const SizedBox(
            height: 10.0,
            ),
            Row(
              children: [
                Container(
                height: 100,
                width: 30,
                decoration: const BoxDecoration(
                color: Colors.blue,
                ),
                ),
                const SizedBox(
                width: 10.0,
                ),
                Container(
                height: 100,
                width: 30,
                decoration: const BoxDecoration(
                color: Colors.blue,
                ),
                ),
                const SizedBox(
                width: 10.0,
                ),

                Expanded(
                  child: Container(
                  height: 100,
                  width: 100,
                  decoration: const BoxDecoration(
                  color: Colors.blue,
                  ),
                  ),
                ),
              ],
            ),
          ],),
        )
    );
  }
}