# fuzzylogic
Pure Pyhton Fuzzy Logic Implementation. The only 3rd party library used in this project are Math and Matplotlib. Matplotlib is used only for visualization purpose.

## Getting Started

### Prerequisites
fuzzylogic depends on
* Math
* Matplotlib (optional)

# Capability
## Inference Engine
* Mamdani
* Tsukamoto
### Defuzzificaton Method
* First of Maxima
* Mean of Maxima
* Last of Maxima
* Centroid
* Center of Gravity (can not be used on Tsukamoto Inference Engine, use Centroid instead)
* Center of Sum (can not be used on Tsukamoto Inference Engine)
* Weighted Average
### Implication Operator
* Dienes Rescher
* Lukasiewicz
* Zadeh
* Godel
* Mamdani Minimum
* Mamdani Product
* Tsukamoto (unofficial operator, created only for flexibility purpose)
### Intersection Operator
* Zadeh (Minimum)
* Dombi
* Dubois
* Yager
* Drastic Product
* Einstein Product
* Algebraic Product
### Union Operator
* Zadeh (Maximum)
* Dombi
* Dubois
* Yager
* Drastic Sum
* Einstein Sum
* Algebraic Sum
### Complement Operator
* Zadeh
* Sugeno
* Yager
#### Membership Function
* Linear
* Triangular
* Trapezoid
* Gaussian

## Running the Example
To see the result of this example just simpy run "Fuzzy Example.py" on your Python IDE.

In this example we are going to predict the price of flat rental based on : 
* Distance from nearby university   (meter)
* Area of the flat                  (meter^2)
* Facility                          (percent)

Suppose we're using Tsukamoto Inference Engine. Then the operators we're going to use are :
* Intersection : Zadeh
* Union : Zadeh
* Implication : Tsukamoto

### 1. Defining Linguistic Variables and Their Domain

* Distance (200 <= X <= 10000) in meter
  * Near
  * Mid
  * Far
* Area (4 <= X <= 20) in meter^2
  * Small
  * Large
* Facility (0 <= X <= 100) in percent (%)
  * Common
  * Full
* Price (250 <= X <= 1500) in 10^3 Rupiah
  * Cheap
  * Medium
  * High
  
```python
distance = mf.linspace(200,10000,98001)
area = mf.linspace(4,20,16001)  
facility = mf.linspace(0,100,10001)
price = mf.linspace(250,1500,12501)    
```
note that there are 98001 points between 200 and 10000 inlcuding themselves. More points means more accurate.

### 2. Defining Fuzzy Set and Their Membership

* Distance (200 <= X <= 10000) in meter
  * Near, trapezoid
  * Mid, trapezoid
  * Far, trapezoid
* Area (4 <= X <= 20) in meter^2
  * Small, trapezoid
  * Large, tapezoid
* Facility (0 <= X <= 100) in percent (%)
  * Common, trapezoid
  * Full, trapezoid
* Price (250 <= X <= 1500) in 10^3 Rupiah
  * Cheap, negative slope line
  * Medium, trapezoid
  * High, trapezoid

After defining their membership function, we can calculate membership degree corresponding to their domain.

* Distance Variable
  ```python
  distanceNear = ["trapmf",-math.inf,-math.inf,2000,4000]
  distanceNearMf = mf.membership(distanceNear, distance)
  distanceMid = ["trapmf",2000,4000,6000,8000]
  distanceMidMf = mf.membership(distanceMid, distance)
  distanceFar = ["trapmf",6000,8000,math.inf,math.inf]
  distanceFarMf = mf.membership(distanceFar, distance)
  ```
![Distance Variable](/figure/distance.png)

* Area Variable
  ```python
  areaSmall = ["trapmf",-math.inf,-math.inf,8,10]
  areaSmallMf = mf.membership(areaSmall, area)
  areaLarge = ["trapmf",8,10,math.inf,math.inf]
  areaLargeMf = mf.membership(areaLarge, area)
  ```
![Area Variable](/figure/area.png)

* Facility Variable
  ```python
  facilityCommon = ["trapmf",-math.inf,-math.inf,20,40]
  facilityCommonMf = mf.membership(facilityCommon, facility)
  facilityFull = ["trapmf",20,40,math.inf,math.inf]
  facilityFullMf = mf.membership(facilityFull, facility)
  ```
![Facility Variable](/figure/facility.png)

* Price Variable
  ```python
  price1Cheap = ["linenegmf",250,450]
  price1CheapMf = mf.membership(price1Cheap, price)
  price1Med = ["trapmf",400,500,750,750]
  price1MedMf = mf.membership(price1Med, price)
  price1High = ["trapmf",750,1000,math.inf,math.inf]
  price1HighMf = mf.membership(price1High, price)
  ```
![Price Variable](/figure/price.png)

### 3. Defining Input
This system takes fuzzy set singleton as input. For this example we use 3 variables as input and 1 value each of them. 
Suppose we want a flat with distance 2500 m, area 12 m^2, and facility 60%.
  ```python
inpDistance = [2500]
inpArea = [12]
inpFacility = [60]
  ```
### 4. Defining Rules and Compute Them with the Input
Suppose we define 12 rules for our system, there are:
#Rule Base
1. IF Near AND Small AND Common THEN Cheap
2. IF Near AND Large AND Common THEN High
3. IF Near AND Small AND Full THEN Medium
4. IF Near AND  Large AND Full THEN High
5. IF Mid AND Small AND Common THEN Cheap
6. IF Mid AND Large AND Common THEN Medium
7. IF Mid AND Small AND Full THEN Medium
8. IF Mid AND Large AND Full THEN High
9. IF Far AND Small AND Common THEN Medium
10. IF Far AND Large AND Common THEN High
11. IF Far AND Small AND Full THEN Medium
12. IF Far AND Large AND Full THEN High

#### 1. IF Near AND Small AND Common THEN Cheap
  ```python
inpDistanceMf = mf.membership(distanceNear, inpDistance)
inpAreaMf = mf.membership(areaSmall, inpArea)
inpFacilityMf = mf.membership(facilityCommon, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule1 = imp.tsukamotoImp(antecedent,price1CheapMf)
  ```
![Output Rule 1](/figure/rule1.png)

```
alpha-predicate1 = 0
z1 = 250
```

For every rule we compute, we should clear the membership of input and antecedent because their value in each iteration would be different, so we can use the same variable in every rule.

  ```python
inpDistanceMf.clear()
inpAreaMf.clear()
inpFacilityMf.clear()
antecedent.clear()
  ```
#### 2. IF Near AND Large AND Common THEN High
  ```python
inpDistanceMf = mf.membership(distanceNear, inpDistance)
inpAreaMf = mf.membership(areaLarge, inpArea)
inpFacilityMf = mf.membership(facilityCommon, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule2 = imp.tsukamotoImp(antecedent,price1HighMf)
  ```
![Output Rule 2](/figure/rule2.png)  
 ```
alpha-predicate2 = 0.25
z2 = 812.5
```
#### 3. IF Near AND Small AND Full THEN Medium
  ```python
inpDistanceMf = mf.membership(distanceNear, inpDistance)
inpAreaMf = mf.membership(areaSmall, inpArea)
inpFacilityMf = mf.membership(facilityFull, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule3 = imp.tsukamotoImp(antecedent,price1MedMf)
  ```
![Output Rule 3](/figure/rule3.png)
 ```
alpha-predicate3 = 0
z3 = 250
```
#### 4. IF Near AND  Large AND Full THEN High
  ```python
inpDistanceMf = mf.membership(distanceNear, inpDistance)
inpAreaMf = mf.membership(areaLarge, inpArea)
inpFacilityMf = mf.membership(facilityFull, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule4 = imp.tsukamotoImp(antecedent,price1HighMf)
  ```
![Output Rule 4](/figure/rule4.png)
 ```
alpha-predicate4 = 0.75
z4 = 937.5
```
#### 5. IF Mid AND Small AND Common THEN Cheap
  ```python
inpDistanceMf = mf.membership(distanceMid, inpDistance)
inpAreaMf = mf.membership(areaSmall, inpArea)
inpFacilityMf = mf.membership(facilityCommon, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule5 = imp.tsukamotoImp(antecedent,price1CheapMf)
  ```
![Output Rule 5](/figure/rule5.png)
 ```
alpha-predicate5 = 0
z5 = 250
```
#### 6. IF Mid AND Large AND Common THEN Medium
  ```python
inpDistanceMf = mf.membership(distanceMid, inpDistance)
inpAreaMf = mf.membership(areaLarge, inpArea)
inpFacilityMf = mf.membership(facilityCommon, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule6 = imp.tsukamotoImp(antecedent,price1MedMf)
  ``` 
![Output Rule 6](/figure/rule6.png)
 ```
alpha-predicate6 = 0.25
z6 = 425.0
```
#### 7. IF Mid AND Small AND Full THEN Medium
  ```python
inpDistanceMf = mf.membership(distanceMid, inpDistance)
inpAreaMf = mf.membership(areaSmall, inpArea)
inpFacilityMf = mf.membership(facilityFull, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule7 = imp.tsukamotoImp(antecedent,price1MedMf)
  ```  

![Output Rule 7](/figure/rule7.png)
 ```
alpha-predicate7 = 0
z7 = 250
```
#### 8. IF Mid AND Large AND Full THEN High
  ```python
inpDistanceMf = mf.membership(distanceMid, inpDistance)
inpAreaMf = mf.membership(areaLarge, inpArea)
inpFacilityMf = mf.membership(facilityFull, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule8 = imp.tsukamotoImp(antecedent,price1HighMf)
  ```  
![Output Rule 8](/figure/rule8.png)
 ```
alpha-predicate8 = 0.25
z8 = 812.5
```
#### 9. IF Far AND Small AND Common THEN Medium
  ```python
inpDistanceMf = mf.membership(distanceFar, inpDistance)
inpAreaMf = mf.membership(areaSmall, inpArea)
inpFacilityMf = mf.membership(facilityCommon, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule9 = imp.tsukamotoImp(antecedent,price1MedMf)
  ```  
![Output Rule 9](/figure/rule9.png)
 ```
alpha-predicate9 = 0
z9 = 250
```
#### 10. IF Far AND Large AND Common THEN High
  ```python
inpDistanceMf = mf.membership(distanceFar, inpDistance)
inpAreaMf = mf.membership(areaLarge, inpArea)
inpFacilityMf = mf.membership(facilityCommon, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule10 = imp.tsukamotoImp(antecedent,price1HighMf)
  ```  
![Output Rule 10](/figure/rule10.png)
 ```
alpha-predicate10 = 0
z10 = 250
```
#### 11. IF Far AND Small AND Full THEN Medium
  ```python
inpDistanceMf = mf.membership(distanceFar, inpDistance)
inpAreaMf = mf.membership(areaSmall, inpArea)
inpFacilityMf = mf.membership(facilityFull, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule11 = imp.tsukamotoImp(antecedent,price1MedMf)
  ```  
![Output Rule 11](/figure/rule11.png)
 ```
alpha-predicate11 = 0
z11 = 250
```
#### 12. IF Far AND Large AND Full THEN High
  ```python
inpDistanceMf = mf.membership(distanceFar, inpDistance)
inpAreaMf = mf.membership(areaLarge, inpArea)
inpFacilityMf = mf.membership(facilityFull, inpFacility)
antecedent = inter.zadehIn(inpDistanceMf,inpAreaMf,inpFacilityMf)
rule12 = imp.tsukamotoImp(antecedent,price1HighMf)
  ```  
![Output Rule 12](/figure/rule12.png)
 ```
alpha-predicate12 = 0
z12 = 250
```

### 5. Defuzzification
Combining all the rules into one fuzzy set and then transform it into crisp set, so we can acquire the output of our fuzzy system.
  ```python
cent = defuz.centroid(price,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
weiavg = defuz.weightedAverage(price,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
fom = defuz.firstOfMaxima(price,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
lom = defuz.lastOfMaxima(price,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
mom = defuz.meanOfMaxima(price,rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12)
  ``` 
![Output Fuzzy System](/figure/output.png)

For this example, the system will give us output :
```
The following output from the Fuzzy system based on several defuzzification methods:
Centroid : 810.0
Weighted Average : 810.4166666666666
First Of Maxima : 937.5
Last Of Maxima : 937.5
Mean Of Maxima : 937.5
```
```
z* = sum (alpha-predicatei x zi) / sum (alpha-predicatei)
z* = (0+0.24*812.5+0+0.75*937.5+0+0.25*425+0+0.25*812.5+0+0+0+0) / (0+0.25+0+0.75+0+0.25+0+0.25+0+0+0+0)
z* = 810.41666666
```
## Built With

* [Spyder](https://www.spyder-ide.org/) - The Python IDE used
* [Matplotlib](https://matplotlib.org/) - Graph Visualization Module


## Authors

* **Fachry Firdaus** - *Initial work* - [akridaus277](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## Reference
Fuzzy system design used in this example is based on (https://www.academia.edu/9786506/Implementasi_Fuzzy_Tsukamoto_untuk_Penentuan_Harga_Sewa_Kos)

