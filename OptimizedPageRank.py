import pandas as pd
import time as tm
import numpy as np
import random as rd

start = tm.time()
###############################################################################################################################################################################
"Pembuatan DataFrame wg.txt dengan kolom nama-nama nodes dan destination_nodes"
col_names = ["nodes","destination_nodes"]
df = pd.read_csv("D:/wg - Copy.txt",delimiter=':',names=col_names)
print("given dataset: ")
#print(df)
print()
print('info dataset: ') 
#df.info()
print()
###############################################################################################################################################################################
"Manipulasi DataFrame yang missing values"
a = df.select_dtypes(['object'])                                                # memilih DataFrame yang object class untuk dapat digunakan pada .strip() method
df[a.columns] = a.apply(lambda x: x.str.strip())                                # menghilangkan space di destination_nodes
df['destination_nodes'] = df['destination_nodes'].replace('',np.nan)            # menandakan destination_nodes yang kosong dengan NaN
print('dataset filled with nan on empty values: ')
#print(df)
print()
print('info dataset: ')
#df.info()
print()
###############################################################################################################################################################################
"Pembuatan dangling nodes dan nondangling nodes"
#buat HL
HL_without_dangling = HL_without_dangling = dict.fromkeys(df['nodes'],df['destination_nodes'].dropna())   # menggabungkan 2 DataFrame dan menjadikan dictionary
print('HL: ')
#print(HL_without_dangling)
print()
ndf = df['destination_nodes'].replace(np.nan,'')
nHL_with_dangling = dict.fromkeys(df['nodes'],ndf)
dangling_nodes = [x for x in nHL_with_dangling.keys() if nHL_with_dangling[x] == '']
print('dangling nodes: ')
#print(dangling_nodes)
print()
###############################################################################################################################################################################
"Pembuatan p_lama"
n = len(HL_without_dangling) + len(dangling_nodes)
m = 1/len(df)
p_lama1 = dict.fromkeys(HL_without_dangling,m)
p_lama2 = dict.fromkeys(dangling_nodes,m)
p_lama = {**p_lama1,**p_lama2}
print('p_lama: ')
#print(p_lama)
print()
###############################################################################################################################################################################
"Perhitungan rank"
alpha = rd.random()
print('given alpha: ')
#print(alpha)
print()
iter = int(input('masukkan banyak iterasi: '))
for _ in range(iter):
    beta = sum(p_lama[i] for i in dangling_nodes)
    gamma = (alpha*beta + 1 - alpha)/n
    p_baru = {} # dictionary kosong
    for k in p_lama.keys():
        p_baru[k] = gamma
    for j in HL_without_dangling.keys():
        for k in list(map(int, HL_without_dangling[j][1:-1].split(', '))):
            p_baru[k] += alpha*p_lama[j]/len(list(map(int, HL_without_dangling[j][1:-1].split(', '))))
    p_lama = p_baru.copy()
###############################################################################################################################################################################
"Menyimpan hasil p_lama dan p_baru ke file tersendiri"
p_baru_keys = pd.DataFrame(list(p_baru.keys()),columns=['nodes'])
p_baru_values = pd.DataFrame(list(p_baru.values()),columns=['probability'])
p_baru = p_baru_keys.join(p_baru_values)
sorted_p_baru = p_baru.sort_values(by=['nodes'])
export = sorted_p_baru.to_csv (r'D:\p_baru.csv', index = None, header=True)
###############################################################################################################################################################################
end = tm.time()
print("waktu proses: ", end-start, "s")
