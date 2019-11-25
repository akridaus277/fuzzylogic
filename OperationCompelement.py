# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:08:54 2019

@author: Fachry Firdaus
"""

def zadehComp(x):
    for i in range(len(x)):
        x[i]=1-x[i]

def sugenoComp(x,lambd):
    if -1<lambd:
        for i in range(len(x)):
            x[i]=(1-x[i])/(1+lambd*x)
    return None

def yagerComp(x,w):
    if 0<w:
        for i in range(len(x)):
            x[i]=(1-x[i]**w)**(1/2)
    return None

def linspace(x,y,n):
    step = (y - x) / (n - 1)
    return [x + step * i for i in range(n)]

