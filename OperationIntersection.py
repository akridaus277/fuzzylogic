# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:45:21 2019

@author: Fachry Firdaus
"""

def zadehIn(x,*y):
    z = x[:]
    for k in y:
        for i in range(len(z)):
            z[i]=(min(z[i],k[i]))
    return z

def dombiIn(lambd,x,*y):
    z = x[:]
    if 0<=lambd:
        for k in y:
            for i in range(len(z)):
                z[i]=(1/(1+((1/z[i]-1)**(lambd)+(1/k[i]-1)**(lambd))**(1/lambd)))
    else:
        return None
    return z

def duboisIn(alfa,x,*y):
    z = x[:]
    if 0<=alfa<=1:
        for k in y:
            for i in range(len(z)):
                z[i]=((z[i]*k[i])/(max(z[i]*k[i],alfa)))
    else:
        return None
    return z

def yagerIn(w,x,*y):
    z = x[:]
    if 0<=w:
        for k in y:
            for i in range(len(z)):
                z[i]=(1-min(1,((1-z[i])**w+(1-k[i])**w)**(1/w)))
    else:
        return None
    return z

def drasticIn(x,*y):
    z = x[:]
    for k in y:
        for i in range(len(z)):
            if k[i]==1:
                z[i]=(z[i])
            if z[i]==1:
                z[i]=(k[i])
            else:
                z[i]=(0)
    return z

def einsteinIn(x,*y):
    z = x[:]
    for k in y:
        for i in range(len(z)):
            z[i]=((z[i]*k[i])/(2-(z[i]+k[i]-z[i]*k[i])))
    return z

def algebraicIn(x,*y):
    z = x[:]
    for k in y:
        for i in range(len(z)):
            z[i]=(z[i]*k[i])
    return z