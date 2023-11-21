'''
Exercise 1
Tulis sebuah while loop yang menjumlahkan semua angka hingga 100 (termasuk).
'''


counter=0
total=0

while counter <= 100:
    total += counter
    counter += 1

print(total)

'''
Exercise 2
Verifikasi Kata Sandi
Memberikan pengguna tiga kesempatan untuk memasukkan kata sandi dengan benar.
'''

kata_sandi = 'geng'
masukan_kata_sandi = input('Masukkan kata sandi Anda: ')
percobaan = 1

while percobaan < 3 and masukan_kata_sandi != kata_sandi:
    print('Akses ditolak.')
    print()  # pemisah baris
    percobaan += 1
    masukan_kata_sandi = input('Masukkan kata sandi Anda: ')

if masukan_kata_sandi == kata_sandi:
    print('Akses diberikan.')
else:
    print('Terlalu banyak percobaan. Coba lagi nanti.')

'''
Exercise 3
Tulis sebuah loop for yang mengiterasi melalui sebuah string dan mencetak setiap huruf di baris yang berbeda.
'''
kata = 'antartika'
for k in kata:
  print(k)
  
'''
Exercise 4
'''
print('Bilangan Prima')
rentang_angka = int(input('Masukkan sebuah angka sebagai rentang untuk dievaluasi: '))
print()

for angka in range(2, rentang_angka + 1): # semua angka dari 2 hingga akhir (inklusif)
    prima = True # inisialisasi variabel

    for pembagi in range(2, angka): # evaluasi semua pembagi potensial
        if angka % pembagi == 0: # jika pembagi genap ditemukan
            prima = False # angka bukan prima
            break # keluar dari loop

    if prima == True: # jika prima masih benar
        print(angka, end=' ')



