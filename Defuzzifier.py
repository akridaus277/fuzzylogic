# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:52:16 2019

@author: Fachry Firdaus
"""
import OperationUnion as uni
import OperationIntersection as inter


def firstOfMaxima(a,*b):
    z = b[0][:]
    for k in b:
        z=uni.zadehUn(z,k)
    maxima=max(z)
    domains = []
    
    for i in range(len(z)):
        if z[i]==maxima :
            domains.append(a[i])
    return domains[0]
   
def lastOfMaxima(a,*b):
    z = b[0][:]
    for k in b:
        z=uni.zadehUn(z,k)    
    maxima=max(z)
    domains = []
    
    for i in range(len(z)):
        if z[i]==maxima :
            domains.append(a[i])
    return domains[-1]


def meanOfMaxima(a,*b):
    z = b[0][:]
    for k in b:
        z=uni.zadehUn(z,k)
    maxima=max(z)
    domains = []
    
    for i in range(len(z)):
        if z[i]==maxima :
            domains.append(a[i])
    numer = sum(domains)
    denumer = len(domains)
    return numer/denumer

def centroid(a,*b):
    z = b[0][:]
    for k in b:
        z=uni.zadehUn(z,k)
    numer = sum(a[i]*z[i] for i in range(len(a)))
    denumer = sum(z) 
    return numer/denumer


def weightedAverage(a,*b):
    peaks = []
    dom = []
    obsdom = []
    obspeak =[]
    for k in b:
        peak = max(k)
        for i in range(len(k)-1):
            if (k[i]==peak):
                if(k[i]>=k[i-1])and(k[i]>=k[i+1]):
                    dom.append(a[i])
                    peaks.append(k[i])
        if len(dom)>1:
            obsdom.append(((dom[-1]-dom[0])/2)+dom[0])
            
        else:
            obsdom.append(dom[0])
        obspeak.append(peak)
        del dom[:]
        del peaks[:]
    
    numer = sum(obsdom[i]*obspeak[i] for i in range(len(obsdom)))
    denumer = sum(obspeak)
    return numer/denumer
    

def centerOfGravity(a,*b):
    z = b[0][:]
    for k in b:
        z=uni.zadehUn(z,k)
    
    numer = integrate2(1000,a,z)
    denumer = integrate(1000,a,z)
    
    return numer/denumer


def centerOfSum(a,*b):
    area = []
    center = []
    
    for k in b:
        center.append(centroid(a,k))
        area.append(integrate(1000,a,k))
    
    numer = sum(area[i]*center[i] for i in range(len(area)))
    denumer = sum(area)
    
    return numer/denumer


# =============================================================================
# def integrate(N, domain,rule):
#    
#     value=0.0
#     value2=0.0
#     domains = domain[:]
#     for i in range(len(domains)):
#         domains[i] = round(domains[i],2)
#     NN = float(N)
#     a = float(domains[0])         
#     b = float(domains[-1])
#     for n in range(1,N+1):
#         value +=  rule[domains.index(round((a+ ((n-(1.0/2.0))*((b-a)/NN))),0))]
#         
#     value2 = ((b-a)/NN)*value
#     
#     return value2
#     
# def integrate2(N, domain,rule):
#     
#     value=0.0
#     value2=0.0
#     domains = domain[:]
#     for i in range(len(domains)):
#         domains[i] = round(domains[i],2)
#     NN = float(N)
#     a = float(domains[0])         
#     b = float(domains[-1])
#     for n in range(1,N+1):
#         value +=  rule[domains.index(round((a+ ((n-(1.0/2.0))*((b-a)/NN))),0))]*(domains.index(round((a+ ((n-(1.0/2.0))*((b-a)/NN))),0)))
#     value2 = ((b-a)/NN)*value
#     
#     return value2    
# =============================================================================
    
def integrate(n,domains,rule):
   a = float(domains[0])         
   b = float(domains[-1])  
    
   h = float((b-a)/n)
   result = 0.0
   for i in range(n):
       result += rule[domains.index(round(((a + h/2.0) + i*h),0))]  #f((a + h/2.0) + i*h)
   result *= h
   return result 

def integrate2(n,domains,rule):
   a = float(domains[0])         
   b = float(domains[-1])  
    
   h = float((b-a)/n)
   result = 0.0
   for i in range(n):
       result += rule[domains.index(round(((a + h/2.0) + i*h),0))] * domains.index(round(((a + h/2.0) + i*h),0))  #f((a + h/2.0) + i*h)
   result *= h
   return result 

