'''
Challenge 1

Minta pengguna dengan fungsi input untuk memasukkan 2 angka,
tambahkan, kurangkan, bagikan, dan kalikan angka-angka tersebut, dan cetak hasilnya
'''

# Meminta pengguna memasukkan angka pertama
angka1 = float(input("Masukkan angka pertama: "))

# Meminta pengguna memasukkan angka kedua
angka2 = float(input("Masukkan angka kedua: "))

# Menambahkan angka-angka tersebut
hasil_tambah = angka1 + angka2
print("Hasil penambahan:", hasil_tambah)

# Mengurangkan angka-angka tersebut
hasil_kurang = angka1 - angka2
print("Hasil pengurangan:", hasil_kurang)

# Membagikan angka-angka tersebut
hasil_bagi = angka1 / angka2
print("Hasil pembagian:", hasil_bagi)

# Mengalikan angka-angka tersebut
hasil_kali = angka1 * angka2
print("Hasil perkalian:", hasil_kali)

'''
Challenge 2

Menentukan apakah seorang mahasiswa dapat mendaftar dalam suatu kelas berdasarkan kriteria-kriteria berikut.

- Orang tersebut harus menjadi mahasiswa yang sedang terdaftar saat ini.
- Orang tersebut harus telah menyelesaikan kelas prasyarat atau lulus ujian penempatan.
'''

pendaftaran = input('Apakah Anda seorang mahasiswa yang sedang terdaftar semester ini? (ya/tidak) ')

if pendaftaran == 'ya':
    prasyarat = input('Apakah Anda telah menyelesaikan kursus prasyarat? (ya/tidak) ')
    if prasyarat == 'ya':
        print('Anda dapat mengikuti kursus ini.')
    else: # atau elif prasyarat != 'ya':
        ujian = input('Apakah Anda lulus ujian penempatan? (ya/tidak) ')
        if ujian == 'ya':
            print('Anda dapat mengikuti kursus ini.')
        else:
            print('Silakan selesaikan kelas prasyarat atau ikuti ujian penempatan.')
else:
    print('Anda harus terdaftar semester ini untuk mengikuti kelas ini.')
