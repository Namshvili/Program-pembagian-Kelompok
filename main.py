import random
import numpy as np

print("Program Bagi Kelompok")
print("Bagi kelompok Berdasarkan : ")
print("[1] Nomor Absen")
print("[2] Input Nama")

pilih = input("Masukkan Pilihan: ")

if pilih == "1":
    jum = int(input("Masukkan Jumlah Siswa: "))
    anggota = int(input("Masukkan jumlah Anggota Kelompok: "))
    rage = anggota

    randomList = list(np.random.permutation(np.arange(1,jum+1))[:jum])   
    result = []
    
    for i in range(0, len(randomList), rage):
        n = randomList[i:rage]
        result.append(n)
        rage+=anggota

    for i in range(0, len(result)):
        nomorAbsen = result[i]
        
        print("Kelompok", i+1)
        print("Nomor Absen :", end=" ")
        
        for item in nomorAbsen:
            print(item, end=" ")
        
        print("\r")
        print("======================")
else:
    pass