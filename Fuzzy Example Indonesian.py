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

#Contoh ini menggunakan mesin inferensi Tsukamoto
#Dengan operasi-operasi sebagai berikut :
#Union = min
#Intersection = max
#Implikasi = tsukamoto (khusus pada inferensi tsukamoto)


#Domain
jarak = mf.linspace(0,10000,10001)
luas = mf.linspace(0,20,2001)  
fasilitas = mf.linspace(0,100,101)
harga = mf.linspace(250,1000,75001)   

#Fuzzy Set
jarakDekat = ["trapmf",-math.inf,-math.inf,2000,4000]
jarakDekatMf = mf.membership(jarakDekat, jarak)
plt.plot(jarak,jarakDekatMf, label = "Dekat")
jarakSedang = ["trapmf",2000,4000,6000,8000]
jarakSedangMf = mf.membership(jarakSedang, jarak)
plt.plot(jarak,jarakSedangMf, label = "Sedang")
jarakJauh = ["trapmf",6000,8000,math.inf,math.inf]
jarakJauhMf = mf.membership(jarakJauh, jarak)
plt.plot(jarak,jarakJauhMf,  label = "Jauh")
plt.xlabel('Jarak (m)')
plt.ylabel('Membership')
plt.title('Jarak Kontrakan ke Kampus')
plt.legend()
plt.show()

luasSempit = ["trapmf",-math.inf,-math.inf,8,10]
luasSempitMf = mf.membership(luasSempit, luas)
plt.plot(luas,luasSempitMf, label = "Sempit")
luasLuas = ["trapmf",8,10,math.inf,math.inf]
luasLuasMf = mf.membership(luasLuas, luas)
plt.plot(luas,luasLuasMf,  label = "Luas")
plt.xlabel('Luas (m2)')
plt.ylabel('Membership')
plt.title('Luas Kontrakan')
plt.legend()
plt.show()


fasilitasBiasa = ["trapmf",-math.inf,-math.inf,30,70]
fasilitasBiasaMf = mf.membership(fasilitasBiasa, fasilitas)
plt.plot(fasilitas,fasilitasBiasaMf,  label = "Biasa")
fasilitasLengkap = ["trapmf",30,70,math.inf,math.inf]
fasilitasLengkapMf = mf.membership(fasilitasLengkap, fasilitas)
plt.plot(fasilitas,fasilitasLengkapMf,  label = "Lengkap")
plt.xlabel('Fasilitas (%)')
plt.ylabel('Membership')
plt.title('Fasilitas Kontrakan')
plt.legend()
plt.show()

harga1Murah = ["linenegmf",250,350]
harga1MurahMf = mf.membership(harga1Murah, harga)
plt.plot(harga,harga1MurahMf,  label = "Murah")
harga1Sedang = ["trapmf",300,350,550,550]
harga1SedangMf = mf.membership(harga1Sedang, harga)
plt.plot(harga,harga1SedangMf,  label = "Sedang")
harga1Mahal = ["trapmf",550,800,math.inf,math.inf]
harga1MahalMf = mf.membership(harga1Mahal, harga)
plt.plot(harga,harga1MahalMf,  label = "Mahal")
plt.xlabel('Fasilitas (10^3 rupiah)')
plt.ylabel('Membership')
plt.title('Harga Kontrakan')
plt.legend()
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

inpJarak = [2500]
inpLuas = [12]
inpFasilitas = [60]

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

#Combine All Rules
ruleall = uni.zadehUn(rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
plt.plot(harga,ruleall)
plt.xlabel('Harga (10^3 rupiah)')
plt.ylabel('Membership')
plt.title('Output Sistem Fuzzy')
plt.show()

cent = defuz.centroid(harga,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
weiavg = defuz.weightedAverage(harga,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
fom = defuz.firstOfMaxima(harga,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
lom = defuz.lastOfMaxima(harga,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
mom = defuz.meanOfMaxima(harga,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)

#Defuzzify
print("Berikut output dari sistem Fuzzy berdasarkan beberapa metode defuzifikasi :")
print("Centroid : {0}".format(cent))
print("Weighted Average : {0}".format(weiavg))
print("First Of Maxima : {0}".format(fom))
print("Last Of Maxima : {0}".format(lom))
print("Mean Of Maxima : {0}".format(mom))


