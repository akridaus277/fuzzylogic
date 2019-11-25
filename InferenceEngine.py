# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:19:02 2019

@author: Fachry Firdaus
"""

import MembershipFunction as mf
import OperationCompelement as comp
import OperationUnion as uni
import OperationIntersection as inter
import OperationImplication as imp
import Defuzzifier as defuz
import math
import matplotlib.pyplot as plt

inpJarak = [500]
inpJarakMf = []
inpLuas = [10]
inpLuasMf = []
inpFasilitas = [60]
inpFasilitasMf = []

#Domain
jarak = mf.linspace(0,10000,10001)
luas = mf.linspace(0,20,2001)  
fasilitas = mf.linspace(0,100,101)
harga = mf.linspace(250,1000,75001)   

#Fuzzy Set
jarakDekat = ["trapmf",-math.inf,-math.inf,2000,4000]
jarakDekatMf = mf.membership(jarakDekat, jarak)
plt.plot(jarak,jarakDekatMf)
jarakSedang = ["trapmf",2000,4000,6000,8000]
jarakSedangMf = mf.membership(jarakSedang, jarak)
plt.plot(jarak,jarakSedangMf)
jarakJauh = ["trapmf",6000,8000,math.inf,math.inf]
jarakJauhMf = mf.membership(jarakJauh, jarak)
plt.plot(jarak,jarakJauhMf)
plt.show()

luasSempit = ["trapmf",-math.inf,-math.inf,8,10]
luasSempitMf = mf.membership(luasSempit, luas)
plt.plot(luas,luasSempitMf)
luasLuas = ["trapmf",8,10,math.inf,math.inf]
luasLuasMf = mf.membership(luasLuas, luas)
plt.plot(luas,luasLuasMf)
plt.show()

fasilitasBiasa = ["trapmf",-math.inf,-math.inf,30,70]
fasilitasBiasaMf = mf.membership(fasilitasBiasa, fasilitas)
plt.plot(fasilitas,fasilitasBiasaMf)
fasilitasLengkap = ["trapmf",30,70,math.inf,math.inf]
fasilitasLengkapMf = mf.membership(fasilitasLengkap, fasilitas)
plt.plot(fasilitas,fasilitasLengkapMf)
plt.show()

harga1Murah = ["linenegmf",250,350]
harga1MurahMf = mf.membership(harga1Murah, harga)
plt.plot(harga,harga1MurahMf)
harga1Sedang = ["trapmf",300,350,550,550]
harga1SedangMf = mf.membership(harga1Sedang, harga)
plt.plot(harga,harga1SedangMf)
harga1Mahal = ["trapmf",550,800,math.inf,math.inf]
harga1MahalMf = mf.membership(harga1Mahal, harga)
plt.plot(harga,harga1MahalMf)
plt.show()

#Rule Base
#1   IF dekat AND sempit AND biasa MAKA murah
#2   IF dekat AND luas AND biasa MAKA mahal
#3   IF dekat AND sempit AND lengkap MAKA sedan
#4   IF dekat AND  luas AND lengkap MAKA mahal
#5   IF sedang AND sempit AND biasa MAKA murah
#6   IF sedang AND luas AND biasa MAKA sedang
#7   IF sedang AND sempit AND lengkap MAKA seda
#8   IF sedang AND luas AND lengkap MAKA mahal
#9   IF jauh AND sempit AND biasa MAKA sedang
#10   IF jauh AND luas AND biasa MAKA mahal
#11   IF jauh AND sempit AND lengkap MAKA sedang
#12   IF jauh AND luas AND lengkap MAKA mahal


#1   IF dekat AND sempit AND biasa MAKA murah
inpJarakMf = mf.membership(jarakDekat, inpJarak)
inpLuasMf = mf.membership(luasSempit, inpLuas)
inpFasilitasMf = mf.membership(fasilitasBiasa, inpFasilitas)
antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule1 = imp.tsukamotoImp(antecedent,harga1MurahMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#2   IF dekat AND luas AND biasa MAKA mahal
inpJarakMf = mf.membership(jarakDekat, inpJarak)

inpLuasMf = mf.membership(luasLuas, inpLuas)

inpFasilitasMf = mf.membership(fasilitasBiasa, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule2 = imp.tsukamotoImp(antecedent,harga1MahalMf)

plt.show()
inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#3   IF dekat AND sempit AND lengkap MAKA sedan
inpJarakMf = mf.membership(jarakDekat, inpJarak)

inpLuasMf = mf.membership(luasSempit, inpLuas)

inpFasilitasMf = mf.membership(fasilitasLengkap, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule3 = imp.tsukamotoImp(antecedent,harga1SedangMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#4   IF dekat AND  luas AND lengkap MAKA mahal
inpJarakMf = mf.membership(jarakDekat, inpJarak)

inpLuasMf = mf.membership(luasLuas, inpLuas)

inpFasilitasMf = mf.membership(fasilitasLengkap, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule4 = imp.tsukamotoImp(antecedent,harga1MahalMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#5   IF sedang AND sempit AND biasa MAKA murah
inpJarakMf = mf.membership(jarakSedang, inpJarak)

inpLuasMf = mf.membership(luasSempit, inpLuas)

inpFasilitasMf = mf.membership(fasilitasBiasa, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule5 = imp.tsukamotoImp(antecedent,harga1MurahMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#6   IF sedang AND luas AND biasa MAKA sedang
inpJarakMf = mf.membership(jarakSedang, inpJarak)

inpLuasMf = mf.membership(luasLuas, inpLuas)

inpFasilitasMf = mf.membership(fasilitasBiasa, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule6 = imp.tsukamotoImp(antecedent,harga1SedangMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#7   IF sedang AND sempit AND lengkap MAKA seda
inpJarakMf = mf.membership(jarakSedang, inpJarak)

inpLuasMf = mf.membership(luasSempit, inpLuas)

inpFasilitasMf = mf.membership(fasilitasLengkap, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule7 = imp.tsukamotoImp(antecedent,harga1SedangMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#8   IF sedang AND luas AND lengkap MAKA mahal
inpJarakMf = mf.membership(jarakSedang, inpJarak)

inpLuasMf = mf.membership(luasLuas, inpLuas)

inpFasilitasMf = mf.membership(fasilitasLengkap, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule8 = imp.tsukamotoImp(antecedent,harga1MahalMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#9   IF jauh AND sempit AND biasa MAKA sedang
inpJarakMf = mf.membership(jarakJauh, inpJarak)

inpLuasMf = mf.membership(luasSempit, inpLuas)

inpFasilitasMf = mf.membership(fasilitasBiasa, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule9 = imp.tsukamotoImp(antecedent,harga1SedangMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#10   IF jauh AND luas AND biasa MAKA mahal
inpJarakMf = mf.membership(jarakJauh, inpJarak)

inpLuasMf = mf.membership(luasLuas, inpLuas)

inpFasilitasMf = mf.membership(fasilitasBiasa, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule10 = imp.tsukamotoImp(antecedent,harga1MahalMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#11   IF jauh AND sempit AND lengkap MAKA sedang
inpJarakMf = mf.membership(jarakJauh, inpJarak)

inpLuasMf = mf.membership(luasSempit, inpLuas)

inpFasilitasMf = mf.membership(fasilitasLengkap, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule11 = imp.tsukamotoImp(antecedent,harga1SedangMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()

#12   IF jauh AND luas AND lengkap MAKA mahal
inpJarakMf = mf.membership(jarakJauh, inpJarak)

inpLuasMf = mf.membership(luasLuas, inpLuas)

inpFasilitasMf = mf.membership(fasilitasLengkap, inpFasilitas)

antecedent = inter.zadehIn(inpJarakMf,inpLuasMf,inpFasilitasMf)
rule12 = imp.tsukamotoImp(antecedent,harga1MahalMf)

inpJarakMf.clear()
inpLuasMf.clear()
inpFasilitasMf.clear()
antecedent.clear()


#Defuzzify
print(defuz.centroid(harga,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12))
print(defuz.weightedAverage(harga,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12))
print(defuz.firstOfMaxima(harga,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12))
print(defuz.lastOfMaxima(harga,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12))
print(defuz.meanOfMaxima(harga,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12))


