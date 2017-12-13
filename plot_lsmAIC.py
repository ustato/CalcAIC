#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import AIC
import LSM


# データ
data = np.loadtxt("lsmdata2_train.csv",delimiter=" ")

# データを表示
# print("data")
# print(data)

# データをわかりやすい配列に格納(pltに使いやすくしたいから)
data_x=[]
data_y=[]
for i in data :
    data_x.append(i[0])
    data_y.append(i[1])

# 次数Nを決定
N = 6

# 次数0からNまで実行
for n in range(N+1) :

    # 実行する次数
    print("N="+str(n))

    # LSMで誤差と重みベクトルcoeを計算
    error, coe = LSM.LSM(data, int(n+1))
    print("error:"+str(error))
    print("coe:"+str(coe[::-1]))

    # ここで，このモデルのAICを計算
    l = AIC.l_MAX(list(coe[::-1]),data_x,data_y)
    print("l="+str(l)+",AIC("+str(n)+")="+str(AIC.AIC(l,n+1)))

    # データをプロット
    plt.plot(data_x, data_y, "o")

    # LSMで得た近似線をプロット
    test_x = np.arange(min(data_x), max(data_x), 0.01)
    plt.plot(test_x, LSM.quation_LSM(coe, test_x))

plt.grid()
plt.show()
