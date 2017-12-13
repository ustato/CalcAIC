#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


# 以下より転載
# (http://www.lifewithpython.com/2014/01/python-flatten-nested-lists.html)
def flatten_with_any_depth(nested_list):
    """深さ優先探索の要領で入れ子のリストをフラットにする関数"""
    # フラットなリストとフリンジを用意
    flat_list = []
    fringe = [nested_list]

    while len(fringe) > 0:
        node = fringe.pop(0)
        # ノードがリストであれば子要素をフリンジに追加
        # リストでなければそのままフラットリストに追加
        if isinstance(node, list):
            fringe = node + fringe
        else:
            flat_list.append(node)

    return flat_list


# モデルのパラメータ数をKとしたとき，
# AIC(K) = -2*(最大対数尤度) +2*K
# AICが小さいほど良いモデルであるとされる．

def l_MAX(a,x,y) :
    """
    概要:　   多項式回帰モデルの最大対数尤度を返す関数
    @param a:各項のパラメータ，a[i]=a_i
    @param x:入力
    @param y:出力
    @return :最大対数尤度
    """
    a = [i for i in [a]]
    a = flatten_with_any_depth(a)
    x = [i for i in [x]]
    x = flatten_with_any_depth(x)
    y = [i for i in [y]]
    y = flatten_with_any_depth(y)

    if (len(x)!=len(y)) :
        return "Error."

    # 標本分散を求める
    n = len(x)
    m = len(a)
    sigma_hat = 0
    for i in range(n) :
        temp = (y[i] - a[0])
        for j in range(1,m) :
            temp += (-a[j]*np.power(x[i],j))
        sigma_hat += temp*temp
    sigma_hat /= n

    # 対数尤度を求める
    loglikelihood = -n/2*(np.log(2*np.pi)+1+np.log(sigma_hat))

    return loglikelihood

def AIC(loglikelihood,K) :
    """
    概要:　               AICを返す関数
    @param loglikelihood:最大対数尤度
    @param K:            パラメータ数
    @return :            AIC(K)
    """
    return (-2*loglikelihood+2*(K+1))

# テストデータで検証
x = np.arange(0,1+0.1,0.1)
x = list(x)
y = [0.012,0.121,-0.0194,-0.0183,-0.032,-0.037,0.196,0.077,0.343,0.448,0.434]
a = 0.138573

# 最大対数尤度は3.23417
l = l_MAX(a,x,y)
print(l,AIC(l,1))

a = [-0.0852364,0.447618]
# 最大対数尤度は8.50008
l = l_MAX(a,x,y)
print(l,AIC(l,2))

a = [0.0602566,-0.522335,0.969953]
# 最大対数尤度は13.37498
l = l_MAX(a,x,y)
print(l,AIC(l,3))

a = [0.078849,-0.817746,1.74463,-0.516453]
# 最大対数尤度は13.53748
l = l_MAX(a,x,y)
print(l,AIC(l,4))
