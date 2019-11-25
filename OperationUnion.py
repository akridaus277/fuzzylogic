# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:25:15 2019

@author: Fachry Firdaus
"""

def zadehUn(x,*y):
    z = x[:]
   
    for k in y:
        for i in range(len(z)):
            z[i]=(max(z[i],k[i]))
    return z
  
        

def dombiUn(lambd,x,*y):
    z = x[:]
    if 0<=lambd:
        for k in y:
            for i in range(len(z)):
                z[i]=(1/(1+((1/z[i]-1)**(-lambd)+(1/k[i]-1)**(-lambd))**(-1/lambd)))
    else:
        return None
    return z

def duboisUn(alfa,x,*y):
    z = x[:]
    if 0<=alfa<=1:
        for k in y:
            for i in range(len(z)):
                z[i]=((z[i]+k[i]-z[i]*k[i]-min(z[i],k[i],1-alfa))/(max(1-z[i],1-k[i],alfa)))
    else:
        return None
    return z

def yagerUn(w,x,*y):
    z = x[:]
    if 0<=w:
        for k in y:
            for i in range(len(z)):
                z[i]=(min(1,(z[i]**w+k[i]**w)**(1/w)))
    else:
        return None
    return z

def drasticUn(x,*y):
    z = x[:]
    for k in y:
        for i in range(len(z)):
            if k[i]==0:
                z[i]=(z[i])
            if x[i]==0:
                z[i]=(k[i])
            else:
                z[i]=(1)
    return z
                

def einsteinUn(x,*y):
    z = x[:]
    for k in y:
        for i in range(len(z)):
            z[i]=((z[i]+y[i])/(1+z[i]*y[i]))
    return z

def algebraicUn(x,*y):
    z = x[:]
    for k in y:
        for i in range(len(z)):
            z[i]=(z[i]+y[i]-z[i]*y[i])
    return z

