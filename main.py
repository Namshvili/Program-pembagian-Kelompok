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
        index = anggota

        if jum >= anggota:
            # Jarak Input dan Output
            print("\r")

            # Membuat elemen list no absen random 
            nomorAbsen =  functions.randomNomorAbsen(jum)

            # Membuat kelompok berdasarkan absen
            result = functions.getNomorAbsenKelompok(anggota, index, nomorAbsen)

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
        namaSiswa = input("Masukkan nama-nama siswa (Ivan, Agus, Asep): ")
        anggota = int(input("Masukkan jumlah Anggota Kelompok: "))
        
        index = anggota
        listSiswa = namaSiswa.split(", ")

        # Membuat list random yang berisi nama siswa
        randomSiswa = functions.randomSiswa(listSiswa)

        # Membuat kelompok berdasarkan list random yang berisi nama siswa
        result = functions.getNamaSiswaKelompok(anggota, index, randomSiswa)

        for i in range(0, len(result)):
            siswa = result[i]
            
            print("Kelompok", i+1)
            print("Nama Anggota :", end=", ")
            
            for item in siswa:
                print(item, end=", ")
            
            print("\r")
            print("======================")

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