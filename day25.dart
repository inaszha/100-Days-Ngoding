import 'package:flutter/material.dart';

class ListViewVH extends StatelessWidget {
  const ListViewVH ({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Binar - ListView"),
        ),
        body: HorizontalListView());
  }
}

class HorizontalListView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        SingleChildScrollView(
          scrollDirection:
              Axis.horizontal, 
          child: Container(
            decoration: BoxDecoration(color: Colors.white),
            child: Row(
              children: <Widget>[
                Kategori(
                    text:
                        'kategori 1'), 
                Kategori(text: 'kategori 2'),
                Kategori(text: 'kategori 3'),
                Kategori(text: 'kategori 4'),
                Kategori(text: 'kategori 5'),
                Kategori(text: 'kategori 6'),
                Kategori(text: 'kategori 7'),
              ],
            ),
          ),
        ),
        Expanded(
          child: SingleChildScrollView(
            scrollDirection:
                Axis.vertical, 
            child: Container(
              decoration: BoxDecoration(color: Colors.white),
              child: Column(
                children: <Widget>[
                  Kategori2(
                      text:
                          'kategori 1'), 
                  Kategori2(text: 'kategori 2'),
                  Kategori2(text: 'kategori 3'),
                  Kategori2(text: 'kategori 4'),
                  Kategori2(text: 'kategori 5'),
                  Kategori2(text: 'kategori 6'),
                  Kategori2(text: 'kategori 7'),
                  Kategori2(text: 'kategori 8'),
                  Kategori2(text: 'kategori 9'),
                  Kategori2(text: 'kategori 10'),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }
}

class Kategori extends StatelessWidget {
  final String text;

  Kategori({required this.text, Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.symmetric(horizontal: 2, vertical: 20),
      width: 100.0,
      height: 40.0,
      decoration: BoxDecoration(
        color: Color.fromARGB(255, 152, 152, 152),
        borderRadius: BorderRadius.circular(20.0),
      ),
      child: Center(
        child: Text(
          text,
          style: TextStyle(color: Colors.white),
        ),
      ),
    );
  }
}

class Kategori2 extends StatelessWidget {
  final String text;

  Kategori2({required this.text, Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.symmetric(vertical: 5),
      width: MediaQuery.of(context).size.width * 0.95,
      height: 80.0,
      decoration: BoxDecoration(
        color: Color.fromARGB(255, 152, 152, 152),
        borderRadius: BorderRadius.circular(20.0),
      ),
      child: Center(
        child: Text(
          text,
          style: TextStyle(color: Colors.white),
        ),
      ),
    );
  }
}
