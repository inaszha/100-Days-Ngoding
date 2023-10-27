import 'package:flutter/material.dart';

class Level extends StatelessWidget { 
  const Level({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("level 2"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Column(
          children: [
            Row(
              children: [
                Expanded(
                  child: Container(
                  child: Padding(
                    padding: const EdgeInsets.all(40.0),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                       children: [
                      Container(
                      height: 150,
                      width: 50,
                      decoration: const BoxDecoration(
                      color:Colors.red,
                      ),
                      ),
                      
                        
                      Container(
                        
                      height: 150,
                      width: 50,
                      decoration: const BoxDecoration(
                      color: Colors.red,
                      ),
                      ),
                      
                    ],
                    ),
                  ),
                  height: 200,
                  width: 200,
                  decoration: const BoxDecoration(
                  color: Colors.blue,
                  ),
                  ),
                ),
                const SizedBox(
                width: 10.0,
                ),
                Container(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Container(
                            height: 35,
                            width: 70,
                            decoration: const BoxDecoration(
                            color: Color.fromARGB(255, 179, 194, 175),
                            ),
                            ),
                            const SizedBox(
                            height: 20.0,
                            ),
                            Container(
                            height: 35,
                            width:70,
                            decoration: const BoxDecoration(
                            color: Color.fromARGB(255, 179, 194, 175),
                            ),
                            ),
                          ],
                        ),
                height: 200,
                width: 100,
                decoration: const BoxDecoration(
                color: Color.fromARGB(255, 33, 243, 44),
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
                child: Row(
                children: [
                  const SizedBox(
                  width: 10.0,
                  ),
                 Expanded(
                    child: Container(
                    height: 50,
                    decoration: const BoxDecoration(
                    color: Colors.blue,
                    ),
                    ),
                  ),
                  const SizedBox(
                  width: 10.0,
                  ),
                ],
                ),
              height: 100,
              decoration: const BoxDecoration(
              color: Color.fromARGB(255, 179, 194, 175),
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
                width: 100,
                decoration: const BoxDecoration(
                color: Color.fromARGB(255, 179, 194, 175),
                ),
                ),
                const SizedBox(
                width: 10.0,
                ),
                Expanded(
                  child: Container(
                    child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Container(
                        height: 80,
                        width: 20,
                        decoration: const BoxDecoration(
                        color: Color.fromARGB(255, 247, 6, 6),
                        ),
                        ),
                        const SizedBox(
                        width: 10.0,
                        ),
                        Container(
                        height: 80,
                        width: 20,
                        decoration: const BoxDecoration(
                        color: Color.fromARGB(255, 247, 6, 6),
                        ),
                        ),
                        const SizedBox(
                        width: 10.0,
                        ),
                        Container(
                        height: 80,
                        width: 20,
                        decoration: const BoxDecoration(
                        color: Color.fromARGB(255, 247, 6, 6),
                        ),
                        ),
                        const SizedBox(
                        width: 10.0,
                        ),
                        Container(
                        height: 80,
                        width: 20,
                        decoration: const BoxDecoration(
                        color: Color.fromARGB(255, 247, 6, 6),
                        ),
                        ),
                        const SizedBox(
                        width: 10.0,
                        ),
                        Container(
                        height: 80,
                        width: 20,
                        decoration: const BoxDecoration(
                        color: Color.fromARGB(255, 247, 6, 6),
                        ),
                        ),
                        const SizedBox(
                        width: 10.0,
                        ),
                        Container(
                        height: 80,
                        width: 20,
                        decoration: const BoxDecoration(
                        color: Color.fromARGB(255, 247, 6, 6),
                        ),
                        ),
                        const SizedBox(
                        width: 10.0,
                        ),
                        Container(
                        height: 80,
                        width: 20,
                        decoration: const BoxDecoration(
                        color: Color.fromARGB(255, 247, 6, 6),
                        ),
                        ),
                        const SizedBox(
                        width: 10.0,
                        ),
                        ],
                        
                      ),
                    ),
                  height: 100,
                  width: 100,
                  decoration: const BoxDecoration(
                  color: Color.fromARGB(255, 179, 194, 175),
                  ),
                  ),
                ),
              ],
            ), 
          ],
        ),
      ), 
      
    );
  }
}