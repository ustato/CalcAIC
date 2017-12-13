#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
            y += W[len_W-1-j] * pow(X[i], j)
        Y.append(y)
    return Y

# 正規化LSM実行関数(戻り値:重みベクトルW)
def regularization_LSM(data, N, LAMBDA) :
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

# LSM実行関数(戻り値:重みベクトルW)
def LSM(data, N) :

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
