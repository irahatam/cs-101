def strong_pwd(pwd):
    '''
    Mengevaluasi apakah sebuah kata sandi kuat atau tidak.
    Mengembalikan True jika kuat, False jika tidak cukup kuat.
    
    Kata sandi yang kuat setidaknya terdiri dari 9 karakter dan mencakup setiap kriteria berikut:
    - Setidaknya satu huruf kapital (uppercase)
    - Setidaknya satu huruf kecil (lowercase)
    - Setidaknya satu angka
    - Setidaknya satu simbol: !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
    '''
    import string    
   
    panjang = False
    huruf_besar = False
    huruf_kecil = False
    angka = False
    simbol = False

    panjang_minimal = 9
    simbol_s = string.punctuation

    if len(pwd) >= panjang_minimal:
        panjang = True

        for c in pwd:
            if c.isalpha():
                if c.isupper():
                    huruf_besar = True
                    
                elif c.islower():
                    huruf_kecil = True
     
            if c.isdigit():
                angka = True

            if c in simbol_s:
                simbol = True
            
    kekuatan = panjang and huruf_besar and huruf_kecil and angka and simbol
    
    return kekuatan

def main():
    kata_sandi = input('Masukkan kata sandi Anda: ')

    if strong_pwd(kata_sandi):
        print('Ini adalah kata sandi yang kuat.')
    else:
        print('Kata sandi ini tidak cukup kuat.')

main()
