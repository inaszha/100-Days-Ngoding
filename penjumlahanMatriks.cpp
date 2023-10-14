#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

// Fungsi untuk menghasilkan matriks dengan data acak
vector<vector<int>> generateRandomMatrix(int baris, int kolom) {
    vector<vector<int>> matriks(baris, vector<int>(kolom, 0));
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            matriks[i][j] = rand() % 100;  // Angka acak antara 0 dan 99
        }
    }
    return matriks;
}

// Fungsi untuk menampilkan matriks
void tampilkanMatriks(const vector<vector<int>>& matriks) {
    for (const vector<int>& baris : matriks) {
        for (int elemen : baris) {
            cout << elemen << "\t";
        }
        cout << endl;
    }
}

int main() {
    srand(static_cast<unsigned>(time(0)));  // Inisialisasi generator bilangan acak

    int baris, kolom;
    cout << "Masukkan jumlah baris untuk matriks: ";
    cin >> baris;
    cout << "Masukkan jumlah kolom untuk matriks: ";
    cin >> kolom;

    vector<vector<int>> matriksA = generateRandomMatrix(baris, kolom);
    vector<vector<int>> matriksB = generateRandomMatrix(baris, kolom);

    cout << "Matriks A: " << endl;
    tampilkanMatriks(matriksA);
    cout << "Matriks B: " << endl;
    tampilkanMatriks(matriksB);

    cout << "Hasil Penjumlahan Matriks: " << endl;
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            cout << matriksA[i][j] + matriksB[i][j] << "\t";
        }
        cout << endl;
    }

    cout << "Hasil Pengurangan Matriks: " << endl;
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            cout << matriksA[i][j] - matriksB[i][j] << "\t";
        }
        cout << endl;
    }

    cout << "Hasil Perkalian Matriks: " << endl;
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            int hasilPerkalian = 0;
            for (int k = 0; k < kolom; k++) {
                hasilPerkalian += matriksA[i][k] * matriksB[k][j];
            }
            cout << hasilPerkalian << "\t";
        }
        cout << endl;
    }

    return 0;
}
