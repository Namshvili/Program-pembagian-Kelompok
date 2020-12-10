import functions
confirm = True

while True:
    print("PROGRAM BAGI KELOMPOK BELAJAR")
    print("Bagi kelompok Berdasarkan : ")
    print("[1] Nomor Absen")
    print("[2] Input Nama")
    print("[3] Keluar")

    pilih = input("Masukkan Pilihan: ")

    if pilih == "1":

        jum = int(input("Masukkan Jumlah Siswa: "))
        anggota = int(input("Masukkan jumlah Anggota Kelompok: "))
        rage = anggota

        if jum >= anggota:
            # Jarak Input dan Output
            print("\r")

            # Membuat elemen list no absen random 
            nomorAbsen =  functions.randomNomorAbsen(jum)

            # Membuat kelompok berdasarkan absen
            result = functions.getKelompok(anggota, rage, nomorAbsen)

            # Looping list Result dan menampilkan output program
            for i in range(0, len(result)):
                nomorAbsen = result[i]
                
                print("Kelompok", i+1)
                print("Nomor Absen :", end=" ")
                
                for item in nomorAbsen:
                    print(item, end=" ")
                
                print("\r")
                print("======================")
        else:
            print("Input Salah!")

    elif pilih == "2":
        print("Coming Soon! Versi 2.0")
        break

    elif pilih == "3":
        break

    else:
        print("Pilihan tidak tersedia!")
        break
    
    # Jarak
    print("\r")

    # Konfirmasi 
    confirm = input('Mau coba lagi? [Y/T] : ')

    if confirm == "t" or confirm == "T":
        break
    elif confirm == "y" or confirm == "Y":
        pass
    else:
        print('Pilihan tidak tersedia!')
        break
# Selesai
print("Terima kasih sudah mencoba!")