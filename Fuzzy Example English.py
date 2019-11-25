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
distance = mf.linspace(0,10000,10001)
area = mf.linspace(0,20,2001)  
facility = mf.linspace(0,100,101)
price = mf.linspace(250,1000,75001)   

#Fuzzy Set
distanceNear = ["trapmf",-math.inf,-math.inf,2000,4000]
distanceNearMf = mf.membership(distanceNear, distance)
plt.plot(distance,distanceNearMf, label = "Near")
distanceMid = ["trapmf",2000,4000,6000,8000]
distanceMidMf = mf.membership(distanceMid, distance)
plt.plot(distance,distanceMidMf, label = "Mid")
distanceFar = ["trapmf",6000,8000,math.inf,math.inf]
distanceFarMf = mf.membership(distanceFar, distance)
plt.plot(distance,distanceFarMf,  label = "Far")
plt.xlabel('Distance (m)')
plt.ylabel('Membership')
plt.title('Distance from Nearby University')
plt.legend()


plt.show()


areaSmall = ["trapmf",-math.inf,-math.inf,8,10]
areaSmallMf = mf.membership(areaSmall, area)
plt.plot(area,areaSmallMf, label = "Small")
areaLarge = ["trapmf",8,10,math.inf,math.inf]
areaLargeMf = mf.membership(areaLarge, area)
plt.plot(area,areaLargeMf,  label = "Large")
plt.xlabel('Area (m2)')
plt.ylabel('Membership')
plt.title('Area of Flat')
plt.legend()
plt.show()


facilityCommon = ["trapmf",-math.inf,-math.inf,30,70]
facilityCommonMf = mf.membership(facilityCommon, facility)
plt.plot(facility,facilityCommonMf,  label = "Common")
facilityFull = ["trapmf",30,70,math.inf,math.inf]
facilityFullMf = mf.membership(facilityFull, facility)
plt.plot(facility,facilityFullMf,  label = "Full")
plt.xlabel('Fasilitas (%)')
plt.ylabel('Membership')
plt.title('Facility of Flat')
plt.legend()
plt.show()


price1Cheap = ["linenegmf",250,350]
price1CheapMf = mf.membership(price1Cheap, price)
plt.plot(price,price1CheapMf,  label = "Cheap")
price1Med = ["trapmf",300,350,550,550]
price1MedMf = mf.membership(price1Med, price)
plt.plot(price,price1MedMf,  label = "Medium")
price1High = ["trapmf",550,800,math.inf,math.inf]
price1HighMf = mf.membership(price1High, price)
plt.plot(price,price1HighMf,  label = "High")
plt.xlabel('Price (10^3 Rupiah)')
plt.ylabel('Membership')
plt.title('Price of Flat Rental')
plt.legend()
plt.show()


#Rule Base
#1   IF Near AND Small AND Common THEN Cheap
#2   IF Near AND Large AND Common THEN High
#3   IF Near AND Small AND Full THEN Medium
#4   IF Near AND  Large AND Full THEN High
#5   IF Mid AND Small AND Common THEN Cheap
#6   IF Mid AND Large AND Common THEN Medium
#7   IF Mid AND Small AND Full THEN Medium
#8   IF Mid AND Large AND Full THEN High
#9   IF Far AND Small AND Common THEN Medium
#10   IF Far AND Large AND Common THEN High
#11   IF Far AND Small AND Full THEN Medium
#12   IF Far AND Large AND Full THEN High

inpDistance = [2500]
inpArea = [12]
inpFacility = [60]

#1   IF dekat AND sempit AND biasa MAKA murah
inpDistanceMf = mf.membership(distanceNear, inpDistance)

inpAreaMf = mf.membership(areaSmall, inpArea)

inpFacilityMf = mf.membership(facilityCommon, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule1 = imp.tsukamotoImp(antecedent,price1CheapMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#2   IF dekat AND luas AND biasa MAKA mahal
inpDistanceMf = mf.membership(distanceNear, inpDistance)

inpAreaMf = mf.membership(areaLarge, inpArea)

inpFacilityMf = mf.membership(facilityCommon, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule2 = imp.tsukamotoImp(antecedent,price1HighMf)

plt.show()
inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#3   IF dekat AND sempit AND lengkap MAKA sedan
inpDistanceMf = mf.membership(distanceNear, inpDistance)

inpAreaMf = mf.membership(areaSmall, inpArea)

inpFacilityMf = mf.membership(facilityFull, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule3 = imp.tsukamotoImp(antecedent,price1MedMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#4   IF dekat AND  luas AND lengkap MAKA mahal
inpDistanceMf = mf.membership(distanceNear, inpDistance)

inpAreaMf = mf.membership(areaLarge, inpArea)

inpFacilityMf = mf.membership(facilityFull, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule4 = imp.tsukamotoImp(antecedent,price1HighMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#5   IF sedang AND sempit AND biasa MAKA murah
inpDistanceMf = mf.membership(distanceMid, inpDistance)

inpAreaMf = mf.membership(areaSmall, inpArea)

inpFacilityMf = mf.membership(facilityCommon, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule5 = imp.tsukamotoImp(antecedent,price1CheapMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#6   IF sedang AND luas AND biasa MAKA sedang
inpDistanceMf = mf.membership(distanceMid, inpDistance)

inpAreaMf = mf.membership(areaLarge, inpArea)

inpFacilityMf = mf.membership(facilityCommon, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule6 = imp.tsukamotoImp(antecedent,price1MedMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#7   IF sedang AND sempit AND lengkap MAKA seda
inpDistanceMf = mf.membership(distanceMid, inpDistance)

inpAreaMf = mf.membership(areaSmall, inpArea)

inpFacilityMf = mf.membership(facilityFull, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule7 = imp.tsukamotoImp(antecedent,price1MedMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#8   IF sedang AND luas AND lengkap MAKA mahal
inpDistanceMf = mf.membership(distanceMid, inpDistance)

inpAreaMf = mf.membership(areaLarge, inpArea)

inpFacilityMf = mf.membership(facilityFull, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule8 = imp.tsukamotoImp(antecedent,price1HighMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#9   IF jauh AND sempit AND biasa MAKA sedang
inpDistanceMf = mf.membership(distanceFar, inpDistance)

inpAreaMf = mf.membership(areaSmall, inpArea)

inpFacilityMf = mf.membership(facilityCommon, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule9 = imp.tsukamotoImp(antecedent,price1MedMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#10   IF jauh AND luas AND biasa MAKA mahal
inpDistanceMf = mf.membership(distanceFar, inpDistance)

inpAreaMf = mf.membership(areaLarge, inpArea)

inpFacilityMf = mf.membership(facilityCommon, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule10 = imp.tsukamotoImp(antecedent,price1HighMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#11   IF jauh AND sempit AND lengkap MAKA sedang
inpDistanceMf = mf.membership(distanceFar, inpDistance)

inpAreaMf = mf.membership(areaSmall, inpArea)

inpFacilityMf = mf.membership(facilityFull, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule11 = imp.tsukamotoImp(antecedent,price1MedMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#12   IF jauh AND luas AND lengkap MAKA mahal
inpDistanceMf = mf.membership(distanceFar, inpDistance)

inpAreaMf = mf.membership(areaLarge, inpArea)

inpFacilityMf = mf.membership(facilityFull, inpFacility)

antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule12 = imp.tsukamotoImp(antecedent,price1HighMf)

inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()

#Combine All Rules
ruleall = uni.zadehUn(rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
plt.plot(price,rule12)
plt.xlabel('Price (10^3 rupiah)')
plt.ylabel('Membership')
plt.title('Rule 12')
plt.show()

cent = defuz.centroid(price,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
weiavg = defuz.weightedAverage(price,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
fom = defuz.firstOfMaxima(price,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
lom = defuz.lastOfMaxima(price,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
mom = defuz.meanOfMaxima(price,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)

#Defuzzify
print("The following output from the Fuzzy system based on several defuzzification methods:")
print("Centroid : {0}".format(cent))
print("Weighted Average : {0}".format(weiavg))
print("First Of Maxima : {0}".format(fom))
print("Last Of Maxima : {0}".format(lom))
print("Mean Of Maxima : {0}".format(mom))


