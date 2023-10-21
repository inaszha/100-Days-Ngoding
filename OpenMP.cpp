#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <omp.h>  // Menambahkan header OpenMP


using namespace std;

// Fungsi untuk menghasilkan matriks dengan data acak
vector<vector<int>> generateRandomMatrix(int baris, int kolom) {
    vector<vector<int>> matriks(baris, vector<int>(kolom, 0));
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < kolom; j++) {
            matriks[i][j] = rand() % 10;  // Angka acak antara 0 dan 9
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

    clock_t startAll = clock();

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
#pragma omp parallel for
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
#pragma omp parallel for
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
#pragma omp parallel for
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

    clock_t endAll = clock();

    cout << "matriks ordo " << baris << " x " << kolom << " :" << endl;

    // Menghitung waktu yang diperlukan untuk Penjumlahan
    double waktuDiperlukanPenjumlahan = static_cast<double>(endPenjumlahan - startPenjumlahan) * 1000.0 / CLOCKS_PER_SEC;
    cout << "Waktu yang diperlukan Komputasi Penjumlahan: " << waktuDiperlukanPenjumlahan << " Milidetik" << endl;

    // Menghitung waktu yang diperlukan untuk Pengurangan
    double waktuDiperlukanPengurangan = static_cast<double>(endPengurangan - startPengurangan) * 1000.0 / CLOCKS_PER_SEC;
    cout << "Waktu yang diperlukan Komputasi Pengurangan: " << waktuDiperlukanPengurangan << " Milidetik" << endl;

    // Menghitung waktu yang diperlukan untuk perkalian
    double waktuDiperlukanPerkalian = static_cast<double>(endPerkalian - startPerkalian) * 1000.0 / CLOCKS_PER_SEC;
    cout << "Waktu yang diperlukan Komputasi Perkalian: " << waktuDiperlukanPerkalian << " Milidetik" << endl;

    // Menghitung waktu yang diperlukan untuk Keseluruhan Prosessing
    double waktuAll = static_cast<double>(endAll - startAll) / CLOCKS_PER_SEC;
    cout << "Waktu yang diperlukan Komputasi Keseluruhan: " << waktuAll << " Detik" << endl;


    return 0;
}
