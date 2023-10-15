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

    // Inisialisasi matriks untuk hasil penjumlahan, pengurangan, dan perkalian
    vector<vector<int>> hasilPenjumlahan(baris, vector<int>(kolom, 0));
    vector<vector<int>> hasilPengurangan(baris, vector<int>(kolom, 0));
    vector<vector<int>> hasilPerkalian(baris, vector<int>(kolom, 0));

    // Mulai mengukur waktu Awal
    clock_t start = clock();

    // Mulai mengukur waktu Penjumlahan
    clock_t startPenjumlahan = clock();

    // Penjumlahan matriks
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            hasilPenjumlahan[i][j] = matriksA[i][j] + matriksB[i][j];
        }
    }

    // Selesai mengukur waktu Penjumlahan
    clock_t endPenjumlahan = clock();

    // Mulai mengukur waktu Pengurangan
    clock_t startPengurangan = clock();

    // Pengurangan matriks
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            hasilPengurangan[i][j] = matriksA[i][j] - matriksB[i][j];
        }
    }

    // Selesai mengukur waktu Pengurangan
    clock_t endPengurangan = clock();


    // Mulai mengukur waktu Perkalian
    clock_t startPerkalian = clock();

    // Perkalian matriks
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            for (int k = 0; k < kolom; k++) {
                hasilPerkalian[i][j] += matriksA[i][k] * matriksB[k][j];
            }
        }
    }

    // Selesai mengukur waktu Perkalian
    clock_t endPerkalian = clock();

    // Selesai mengukur waktu akhir
    clock_t end = clock();

    // Menampilkan hasil penjumlahan matriks
    cout << "Hasil Penjumlahan Matriks:" << endl;
    tampilkanMatriks(hasilPenjumlahan);

    // Menampilkan hasil pengurangan matriks
    cout << "Hasil Pengurangan Matriks:" << endl;
    tampilkanMatriks(hasilPengurangan);



    // Menampilkan hasil perkalian matriks
    cout << "Hasil Perkalian Matriks:" << endl;
    tampilkanMatriks(hasilPerkalian);


    // Menghitung waktu yang diperlukan untuk perkalian
    double waktuDiperlukanPenjumlahan = static_cast<double>(endPenjumlahan - startPenjumlahan) / CLOCKS_PER_SEC;
    cout << "Waktu yang diperlukan Komputasi Penjumlahan: " << waktuDiperlukanPenjumlahan << " detik" << endl;

    // Menghitung waktu yang diperlukan untuk Pengurangan
    double waktuDiperlukanPengurangan = static_cast<double>(endPengurangan - startPengurangan) / CLOCKS_PER_SEC;
    cout << "Waktu yang diperlukan Komputasi Pengurangan: " << waktuDiperlukanPengurangan << " detik" << endl;

    // Menghitung waktu yang diperlukan untuk perkalian
    double waktuDiperlukanPerkalian = static_cast<double>(endPerkalian - startPerkalian) / CLOCKS_PER_SEC;
    cout << "Waktu yang diperlukan Komputasi Perkalian: " << waktuDiperlukanPerkalian << " detik" << endl;

    // Menghitung waktu yang diperlukan untuk Semua Komputasi
    double waktuDiperlukanTotal = static_cast<double>(end - start) / CLOCKS_PER_SEC;
    cout << "Waktu yang diperlukan Semua Komputasi: " << waktuDiperlukanTotal << " detik" << endl;

    return 0;
}\
