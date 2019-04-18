import numpy as np
import time as tm
from collections import Counter
start=tm.time()
print('Selamat datang di simulasi rantai Markov oleh MA')
#meminta ukuran state
n = int(input('Masukkanlah banyak kemungkinan state yang diinginkan: '))

#generate matriks transisi dan vektor peluang awal
#generate matriks dan vektor secara acak
matriks=np.random.rand(n,n)
vektorawal=np.random.rand(n,1)
#mengstokastikkan baris matriks yang muncul
matriks=matriks/matriks.sum(0)
#mengstokastikkan vektor yang muncul
vektorawal=vektorawal/vektorawal.sum(0)

print('Akan digenerate matriks transisi dan vektor peluang awal secara acak...')
print('Matriks transisi awal')
print(matriks)
print(' ')
print('Vektor peluang awal')
print(vektorawal)

#Pada program ini, state yang mungkin dilambangkan dengan 0,1,2,...,n-1.

#1 Menggenerate kejadian-kejadian secara acak dengan peluang sesuai vektor peluang awal
#2 Menentukan state berikutnya dari kejadian-kejadian yang telah digenerate sebelumnya

def fungsipembangkitstate(s,k,v):
    s : int #banyak kejadian awal yang diinginkan
    k : int #banyak state yang mungkin terjadi
    v : np.ndarray #vektor peluang awal
    st=np.random.choice(k,s,replace=True,p=(v[:,0]))
    #membangkitkan kejadian-kejadian awal sesuai input, dan dengan peluang sebesar vektor peluang awal
    return (st)

banstat = int(input('Banyak kejadian awal yang diinginkan: '))
state=fungsipembangkitstate(banstat,n,vektorawal)
print(' ')
print('Kejadian-kejadian awal yang terjadi adalah:')
print(state)

#membangkitkan state setelah iterasi ke-w
def fungsistateselanjutnya(mat,st,k,w):
    mat : np.ndarray #matriks transisi dari rantai markov
    st : np.ndarray #vektor berisi state awal
    k : int #banyakstateyang mungkin terjadi
    w : int #pangkat matriks/banyak iterasi
    new=[]
    mat=np.linalg.matrix_power(mat,w)
    for i in range(len(st)):
        new.append(np.random.choice(k,p=(mat[:,st[i]])))
    return(new)
stateb=fungsistateselanjutnya(matriks,state,n,1)
    
print(' ')
print('State selanjutnya dari kejadian yang digenerate sebelumnya adalah: ')
print(stateb)

#4 Mengetahui kondisi state saat k tertentu
k1=int(input('Mengetahui kondisi state saat k= ' ))
#membuat matriks transisi baru
statek=fungsistateselanjutnya(matriks,state,n,k1)
print('Kondisi saat iterasi ke-',str(k1),' adalah:')
print(statek)
X=Counter(statek)
print('Counter dari banyak state di kejadian di atas adalah: ')
print(X)

#### Vektor Ranknya gimana?
#Generate vektor rank dari simulasi saat waktu k
vekpel=np.zeros((n,1))
for i in X.keys():
    vekpel[int(i)]=X[i]
print('Dari hasil percobaan di iterasi di atas, vektor ranknya adalah: ')
print(vekpel/vekpel.sum(0))
print(' ')
print('Vektor rank-nya adalah: ')
print(np.linalg.matrix_power(matriks,k1).dot(vektorawal))

#3. Menggenerate sebuah simulasi rantai Markov dengan panjang sesuai keinginan
panjangrantai=int(input('Panjang rantai Markov yang ingin disimulasikan: '))
#membuat array simulasi yang berisi kondisi awal
print('Hasil simulasi rantai Markov adalah: ')
def simulasiMarkov(k,v,mat,z):
    k : int #banyak state yang mungkin
    v : np.ndarray #vektor peluang awal
    mat : np.array #matriks transisi dari rantai Markov
    z : int #panjang simulasi
    sim=[int(np.random.choice(k,p=(v.T[0,:])))]
    for i in range(z-1):
    #menambahkan state selanjutnya ke array simulasi sesuai dengan matriks transisi
        sim.append(int(np.random.choice(k,p=(mat[:,int(sim[i])]))))
    return(sim)

simulasi=simulasiMarkov(n,vektorawal,matriks,panjangrantai)
print(simulasi)

#5. membuat matriks transisi dari hasil simulasi
Mbaru=np.zeros((n,n))
#menghitung banyak kemunculan (i,j) di simulasi secara urut 
for (i,j) in zip(simulasi,simulasi[1:]):
    Mbaru[int(j)][int(i)] +=1 
#mengstokastikkan baris matriks yang muncul
Mbaru=Mbaru/Mbaru.sum(0)

#membuat vektor transisi dari hasil simulasi
X=Counter(state)
vekpel=np.zeros((n,1))
for i in X.keys():
    vekpel[int(i)]=X[i]
    
vekpel=vekpel/vekpel.sum(0)
print(' ')
print('Matriks transisi dari simulasi rantai di atas adalah:')
print(Mbaru)
print(' ')
print('Vektor peluang awal dari simulasi rantai di atas adalah:')
print(vekpel)

print('lama waktu: ', tm.time()-start, 's')
