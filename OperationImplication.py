# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:52:22 2019

@author: Fachry Firdaus
"""
def dienesrescherImp(x,y):
    z = []
    for i in range(len(x)):
        for j in range(len(y)):
                z.append(max(1-x[i],y[j]))
    return z
    

def lukasiewiczImp(x,y):
    z = []
    for i in range(len(x)):
        for j in range(len(y)):
            z.append(min(1, 1-x[i]+y[j]))
    return z

def zadehImp(x,y):
    z = []
    for i in range(len(x)):
        for j in range(len(y)):
            z.append(max(min(x[i],y[j]),(1-x[i])))
    return z

def godelImp(x,y,z):
    z = []
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]<=y[j]:
                z.append(1)
            z.append(y[j])
    return z

def mamdaniminImp(x,y):
    z = []
    for i in range(len(x)):
        for j in range(len(y)):
            z.append(min(x[i],y[j]))
    return z

def mamdaniproductImp(x,y):
    z = []
    for i in range(len(x)):
        for j in range(len(y)):
            z.append(x[i]*y[j])
    return z

def tsukamotoImp(x,y):
    z = []
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]==y[j]:
                z.append(x[i])
            else:
                z.append(0)
            
    return z
