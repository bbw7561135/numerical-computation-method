# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:10:46 2017

@author: 大帆
"""

import numpy as np

def Gaussian_elimination(A,Y):
    W=np.c_[A,Y]
    for i,L in enumerate(range(A.shape[0])):
        for m in range(L+1,A.shape[0]):
            W[m]=W[m]-W[L]*(W[m,i]/W[L,i])
            
    x=[]    
    for i in range(A.shape[0])[::-1]:
        sum_=0
        for h,j in enumerate(range(i+1,A.shape[0])):
            sum_+=W[i,j]*x[-1-h]
        x.append((W[i,-1]-sum_)/W[i,i])
        
    x.reverse()
    return x
A=[[1,1,1],
   [2,1,3],
   [5,3,4]]
Y=[6,13,23]
A=np.array(A)
Y=np.array(Y).reshape([-1,1])
print("高斯消去法得到x1,x2,x3为：")
print(Gaussian_elimination(A,Y))
print("矩阵求解得到的结果")
print(np.mat(A).I*np.mat(Y))

def Gaussian_elimination_c(A,Y):
    W=np.zeros(A.shape)
    for i in range(A.shape[0]):
        W[i]=A[i]/A[i].max()
    h=[]
    for i in range(W.shape[0]):
        id_max=np.argmax(W[i:,i])
        h.append(id_max)
        t=W[i].copy()
        W[i]=W[id_max+i]
        W[id_max+i]=t
    del W
    A=A[h]
    Y=Y[h]
    return Gaussian_elimination(A,Y)

A=[[2.0,100],
   [1,1]]
Y=[100,2]
A=np.array(A)
Y=np.array(Y).reshape([-1,1])
print('*'*10)
print("交换高斯消去法得到的 x1,x2为：")
print(Gaussian_elimination_c(A,Y))
print("矩阵求解得到的结果")
print(np.mat(A).I*np.mat(Y))