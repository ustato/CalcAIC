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
