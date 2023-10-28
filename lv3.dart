import 'package:flutter/material.dart';

class Level3 extends StatelessWidget {
  const Level3({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold( 
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Expanded(
                  child: Container(
                    child: 
                    Padding(
                      padding: const EdgeInsets.all(30.0),
                      child: Container(
                      height: 20,
                      width: 20,
                      decoration: const BoxDecoration(
                      color: Colors.red,
                      ),
                      ),
                    ),
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
                Expanded(
                  child: Container(
                    child:
                     Expanded(
                       child: Column(
                         children: [
                           Container(
                          height: 40,
                          decoration: const BoxDecoration(
                          color: Colors.blue,
                          ),
                          ),
                          const SizedBox(
                          height: 20.0,
                          ),
                          Container(
                          height: 40,
                          decoration: const BoxDecoration(
                          color: Colors.blue,
                          ),
                          ),
                         ],
                       ),
                     ),
                  height: 100,
                  width: 100,
                  decoration: const BoxDecoration(
                  color: Colors.white,
                  ),
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
            const SizedBox(
            height: 10.0,
            ),
            Row(
              children: [
                Expanded(
                  child: Container(
                    child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Container(
                          height: 100,
                          width: 40,
                          decoration: const BoxDecoration(
                          color: Colors.red,
                          ),
                          ),
                          const SizedBox(
                          width: 30.0,
                          ),
                          Container(
                          height: 100,
                          width: 40,
                          decoration: const BoxDecoration(
                          color: Colors.red,
                          ),
                          ),
                          const SizedBox(
                          width: 30.0,
                          ),
                          Container(
                          height: 100,
                          width: 40,
                          decoration: const BoxDecoration(
                          color: Colors.red,
                          ),
                          ),
                          
                        ],
                      ),
                    ),
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
                  child: Padding(
                    padding: const EdgeInsets.all(15.0),
                    child: Column(
                      children: [
                        Container(
                        height: 30,
                        width: 100,
                        decoration: const BoxDecoration(
                        color: Colors.red,
                        ),
                        ),
                        const SizedBox(
                        height: 10.0,
                        ),
                        Container(
                        height: 30,
                        width: 100,
                        decoration: const BoxDecoration(
                        color: Colors.red,
                        ),
                        ),
                      ],
                    ),
                  ),
                height: 100,
                width: 150,
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
                  child: Column(
                    children: [
                      Container(
                      height: 40,
                      width: 100,
                      decoration: const BoxDecoration(
                      color: Colors.red,
                      ),
                      ),
                      const SizedBox(
                      height: 20.0,
                      ),
                      Container(
                      height: 40,
                      width: 100,
                      decoration: const BoxDecoration(
                      color: Colors.red,
                      ),
                      ),
                    ],
                  ),
                height: 100,
                width: 100,
                decoration: const BoxDecoration(
                color: Colors.white,
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
                const SizedBox(
                width: 10.0,
                ),
                Container(
                  child: Column(
                    children: [
                      Container(
                      height: 40,
                      width: 100,
                      decoration: const BoxDecoration(
                      color: Colors.red,
                      ),
                      ),
                      const SizedBox(
                      height: 20.0,
                      ),
                      Container(
                      height: 40,
                      width: 100,
                      decoration: const BoxDecoration(
                      color: Colors.red,
                      ),
                      ),
                    ],
                  ),
                height: 100,
                width: 100,
                decoration: const BoxDecoration(
                color: Colors.white,
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