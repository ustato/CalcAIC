#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import LSM_regularization as LSM

#データ
data = np.loadtxt("lsmdata1_train.csv",delimiter=" ")

# データを表示
#print("data")
#print(data)

# データをわかりやすい配列に格納(pltに使いやすくしたいから)
data_x=[]
data_y=[]
for i in data :
    data_x.append(i[0])
    data_y.append(i[1])

# 次数Nを決定
#N = input("N == ")
N = 3

error, coe = LSM.LSM(data, int(N+1))

print("error")
print(error)
print("coe")
print(coe)


plt.plot(data_x, data_y, "o")

test_x = np.arange(min(data_x), max(data_x), 0.1)
plt.plot(test_x, LSM.quation_LSM(coe, test_x))
plt.show()
