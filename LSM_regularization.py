# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

# LSMで作った式のy座標を求める関数
def quation_LSM(W, X) :
    len_X = len(X)
    len_W = len(W)
    Y = []
    for i in range(len_X) :
        y = 0
        for j in range(len_W) :
            y += W[N-1-j] * pow(X[i], j)
        Y.append(y)
    return Y

# 正規化LSM実行関数(戻り値:重みベクトルW)
def regularization_LSM(data_x, data_y, N, LAMBDA) :
    # X・coe = Y
    X = np.zeros([N,N])
    Y = np.zeros([N,1])

    temp = 0
    for i in range(N):
        for j in range(N):
            temp = 0
            for d in data :
                temp += pow(d[0],2*(N-1)-i-j)
            if 2*(N-1)-i-j == 0 :
                temp = len(data)
            X[i][j] = temp

    for i in range(N):
        temp = 0
        for d in data :
            temp += pow(d[0],N-1-i) * d[1]
            Y[i] = temp

    for i in range(N):
        X[i][i] += LAMBDA

    # coe = inverseX・Y
    # coe:重みベクトル
    coe = np.dot(np.linalg.inv(X),Y)
    coe = coe[:,0]

    # error:二乗和誤差
    error = 0
    maked_data = data
    for i in data :
        temp = 0
        for j in range(N) :
            temp += coe[N-1-j] * pow(i[0], j)

        error += pow(i[1] - temp, 2.0)

    #error = error / len(data)
    error /= 2
    error = np.sqrt(error)

    return error, coe



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
N = 1
N = int(N)
N += 1

# ここで，正規化に使用するλを設定
LAMBDA = 0

error, coe = regularization_LSM(data_x, data_y, N, LAMBDA)

print ("error")
print error
print ("coe")
print coe


plt.plot(data_x, data_y, "o")

test_x = np.arange(min(data_x), max(data_x), 0.1)
plt.plot(test_x, quation_LSM(coe, test_x))
plt.show()
