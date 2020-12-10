import functions

print("Program Bagi Kelompok")
print("Bagi kelompok Berdasarkan : ")
print("[1] Nomor Absen")
print("[2] Input Nama")
print("[3] Keluar")

pilih = input("Masukkan Pilihan: ")

if pilih == "1":
    jum = int(input("Masukkan Jumlah Siswa: "))
    anggota = int(input("Masukkan jumlah Anggota Kelompok: "))
    rage = anggota

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
elif pilih == "2":
    print("Coming Soon! Versi 2.0")
else:
    print("Pilihan tidak tersedia!")
