import 'package:flutter/material.dart';

class RK extends StatelessWidget {
  const RK({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("row dan column"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(children: [
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
              width: 60,
              decoration: const BoxDecoration(
              color: Colors.blue,
              ),
              ),
              const SizedBox(
              width: 10.0,
              ),
              Container(
              height: 100,
              width: 60,
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
            width: MediaQuery.of(context).size.width*0.10,
            decoration: const BoxDecoration(
            color: Colors.blue,
            ),
            ),
            const SizedBox(
            width: 10.0,
            ),
            Container(
            height: 100,
            width: MediaQuery.of(context).size.width*0.10,
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
              decoration: const BoxDecoration(
              color: Colors.blue,
              ),
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
            width: 100,
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