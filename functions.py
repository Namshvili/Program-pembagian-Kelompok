import random
import numpy as np

def randomNomorAbsen(jum):
    return list(np.random.permutation(np.arange(1,jum+1))[:jum])

def getKelompok(anggota, rage, NomorAbsen):
    kelompok = []
    
    for i in range(0, len(NomorAbsen), rage):
        n = NomorAbsen[i:rage]
        kelompok.append(n)
        rage+=anggota
    
    return kelompok