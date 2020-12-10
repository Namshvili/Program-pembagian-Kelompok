import random
import numpy as np

def randomNomorAbsen(jum):
    return list(np.random.permutation(np.arange(1,jum+1))[:jum])

def getNomorAbsenKelompok(anggota, index, NomorAbsen):
    kelompok = []
    
    for i in range(0, len(NomorAbsen), index):
        n = NomorAbsen[i:index]
        kelompok.append(n)
        index+=anggota
    
    return kelompok

def randomSiswa(listSiswa):
    random.shuffle(listSiswa)
    random.shuffle(listSiswa)
    random.shuffle(listSiswa)
    random.shuffle(listSiswa)
    random.shuffle(listSiswa)
    random.shuffle(listSiswa)
    random.shuffle(listSiswa)
    random.shuffle(listSiswa)
    random.shuffle(listSiswa)
    random.shuffle(listSiswa)
    return listSiswa

def getNamaSiswaKelompok(anggota, index, randomSiswa):
    siswa = []

    for i in range(0, len(randomSiswa), index):
        n = randomSiswa[i:index]
        siswa.append(n)
        index+=anggota

    return siswa