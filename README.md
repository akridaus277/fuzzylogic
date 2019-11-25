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

In this example we are going to predict the price of flat rental based on : 
* Distance from nearby university   (meter)
* Area of the flat                  (meter^2)
* Facility                          (percent)

Suppose we're using Tsukamoto Inference Engine. Then the operators we're going to use are :
* Intersection : Zadeh
* Union : Zadeh
* Implication : Tsukamoto

### 1. Defining Linguistic Variables and Their Domain

* Distance (0 <= X <= 10000) in meter
  * Near
  * Mid
  * Far
* Area (0 <= X <= 20) in meter^2
  * Small
  * Large
* Facility (0 <= X <= 100) in percent (%)
  * Common
  * Full
* Price (0 <= X <= 1000) in Rupiah
  * Cheap
  * Medium
  * High
  
```python
distance = mf.linspace(0,10000,10001)
area = mf.linspace(0,20,2001)  
facility = mf.linspace(0,100,101)
price = mf.linspace(250,1000,75001) 
```
note that there are 10001 points between 0 and 10000 inlcuding themselves.

### 2. Defining Fuzzy Set and Their Membership

* Distance (0 <= X <= 10000) in meter
  * Near, trapezoid
  * Mid, trapezoid
  * Far, trapezoid
* Area (0 <= X <= 20) in meter^2
  * Small, trapezoid
  * Large, tapezoid
* Facility (0 <= X <= 100) in percent (%)
  * Common, trapezoid
  * Full, trapezoid
* Price (0 <= X <= 1000) in Rupiah
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
* Area Variable
  ```python
  areaSmall = ["trapmf",-math.inf,-math.inf,8,10]
  areaSmallMf = mf.membership(areaSmall, area)
  areaLarge = ["trapmf",8,10,math.inf,math.inf]
  areaLargeMf = mf.membership(areaLarge, area)
  ```
* Facility Variable
  ```python
  facilityCommon = ["trapmf",-math.inf,-math.inf,30,70]
  facilityCommonMf = mf.membership(facilityCommon, facility)
  facilityFull = ["trapmf",30,70,math.inf,math.inf]
  facilityFullMf = mf.membership(facilityFull, facility)
  ```
* Price Variable
  ```python
  price1Cheap = ["linenegmf",250,350]
  price1CheapMf = mf.membership(price1Cheap, price)
  price1Med = ["trapmf",300,350,550,550]
  price1MedMf = mf.membership(price1Med, price)
  price1High = ["trapmf",550,800,math.inf,math.inf]
  price1HighMf = mf.membership(price1High, price)
  ```
### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
