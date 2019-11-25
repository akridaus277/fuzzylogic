# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:34:10 2019

@author: Fachry Firdaus
"""


import math


def triangularMf(x,a,b,c):
    z = []
    for i in range(len(x)):
        if x[i]<= a:
            z.append(0)
        if a<x[i]<=b:
            z.append((x[i]-a)/(b-a))
        if b<x[i]<=c:
            z.append((c-x[i])/(c-b))
        if c<x[i]:
            z.append(0)
    return z
    

def trapezoidMf(x,a,b,c,d):
    z = []
    for i in range(len(x)):
        if x[i]<= a:
            z.append(0)
        if a<x[i]<=b:
            z.append((x[i]-a)/(b-a))
        if b<x[i]<=c:
            z.append(1)
        if c<x[i]<=d:
            z.append((d-x[i])/(d-c))
        if d<x[i]:
            z.append(0)
    return z      
    
    
def gaussianMf(x,center,standardDeviation):
    z = []
    for i in range(len(x)):
        z.append(math.exp((-0.5)*((x[i]-center)/standardDeviation)**2))
    return z

def linspace(x,y,n):
    N = float(n)
    step = (y - x) / (N - 1)
    z = []
    for i in range(n):
        z.append(x+step*float(i))
    return z

def linPosMf(x,a,b):
    z = []
    for i in range(len(x)):
        if x[i]<= a:
            z.append(0)
        if a<x[i]<=b:
            z.append((x[i]-a)/(b-a))
        
        if b<x[i]:
            z.append(0)
    return z

def linNegMf(x,a,b):
    z = []
    for i in range(len(x)):
        if x[i]<= a:
            z.append(0)
        
        if a<x[i]<=b:
            z.append((b-x[i])/(b-a))
        if b<x[i]:
            z.append(0)
    return z

def membership(fuzzySet, domain):
    z = []
    if fuzzySet[0]=="trimf":
        z = triangularMf(domain,fuzzySet[1],fuzzySet[2],fuzzySet[3])
    if fuzzySet[0]=="trapmf":
        z = trapezoidMf(domain,fuzzySet[1],fuzzySet[2],fuzzySet[3],fuzzySet[4])
    if fuzzySet[0]=="gaussmf":
        z = gaussianMf(domain,fuzzySet[1],fuzzySet[2])
    if fuzzySet[0]=="lineposmf":
        z = linPosMf(domain,fuzzySet[1],fuzzySet[2])
    if fuzzySet[0]=="linenegmf":
        z = linNegMf(domain,fuzzySet[1],fuzzySet[2])
        
    return z