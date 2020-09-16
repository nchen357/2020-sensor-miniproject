---
<p align = "center"><b>Memorandum</b></p>

---

**TO:** EC463 Professors

**FROM:** EC463 Students Nicole Chen (U82335685) and Ye Chen (U30225486)

**SUBJECT:** 2020 Sensor Miniproject

**DATE:** September 17, 2020

**PURPOSE**
	The goal of this memo is to report our findings and methodologies in programming the sensor algorithms as well as answer any conceptual questions posed throughout the project.

---

**DISCUSSION**

**Part One: Data flow**
	The 2020 Sensor Miniproject is a python based project that utilizes IoT simulators to simulate data; Upon activating the IoT simulators, we were met with the following message:
> ECE Senior Capstone IoT Simulator

**Part Two: Analysis**
After confirming the IoT simulators functions, we proceeded to save the outputted data into a data.json file, wrote a script to analyze the data and found various measurements for a specific room of our choice - class 1. We have included the specific data set we are analyzing in this repository. Our measurements are as follows:

Temperature | Median | Variance
------------|--------|----------
Class1 | 27.00 | 1058.98

Occupancy| Median | Variance
------------|--------|----------
Class1 | 19.0 | 18.94

Time Interval| Median | Variance
------------|--------|----------
Class1 |  1.01 | 1.09

Our recorded probability functions for various parameters:

![image](https://i.imgur.com/d9BF8b3.png)
![image](https://i.imgur.com/tgSoupK.png)
![image](https://i.imgur.com/MAksoh7.png)
![image](https://i.imgur.com/xT8iE5L.png)

#### 4. Does this mimic a well known distribution for connection intervals in large systems?
This distribution seems to mimic the Erlang distribution. 

**Part Three: Design**
#### 1. Implement an algorithm that detects anomalies in temperature sensor data.
This tuning is performed via our script, anomaly.py, where only data points that are within 2 standard deviations of the average are included. We decided to implement this algorithm because it was sufficient enough to eliminate our outliers without being too strict and eliminating too much of our data points. From these parameters, the measurements are ran again for class 1.

> Readjusted Temperature Data
* Median: 26.99
* Variance: 20.84
* Percentage of total data that has been excluded: 0.3783%

New probability function for adjusted data:

![image](https://i.imgur.com/EybAYkh.png)

#### 2. Does a persistent change in temperature always indicate a failed sensor?
The readjusted data is far more consistent and it appears to prove that less than 5% of the data is drastically skewing the distribution. Stray and extreme values such as these should be rightfully removed to get properly tuned data. If these extreme data points were more persistent and constituted a larger percentage of the data (upwards of 5% and over), then it could possibly indicate a failed or failing sensor.

#### 3. What are possible bounds on temperature for each room type?
From these findings, we can conclude that at least 2 standard deviations from the mean would be a feasible bounds on temperature. In Class 1's case, this bound would be from 1.91 to 52.39 degrees.

**Part four: Conclusion**

#### 1. How is this simulation reflective of the real world?
The simulation does appear to be reflective of the real world - with so many physical and sometimes unpredictable variables, sensors in the real world also tend to have drastic but momentary changes in temperature. The amount of these spikes is typically very low and can be easily tuned out, just as we have observed with the simulated sensors where we used our filtering algorithm to remove any outliers. Overall our data was very consistent, with numbers hovering around ~20-30 degrees, which is realistic given that we are gathering information from a singular room that most likely does not have that many environmental changes.

#### 2. How is this simulation deficient? What factors does it fail to account for?
This simulation does have a few drawbacks however, and without real world parameters there can only be so much these sensors can emulate with proper accuracy. The random number generation for formulating the sensor data may either not be accurate enough or could possibly be even too predictable in comparison with the real world. In a more realistic simulation of the real world, there would be times where our temperature would increase or decrease due to changes in the weather but ours remains relatively constant. Our lack of hardware components also means that while our software simulation is interesting, it leaves us unable to account for any skew in our data caused by deviation in physical variables which would make testing potentially inaccurate during a field test.

#### 3. How is the difficulty of initially using this Python websockets library as compared to a compiled language like C++ websockets?
On the software side, however, the Python coding has been smooth and overall the websockets library is quite convenient. Python was also extremely convenient when parsing through each of the strings and with the abundance of libraries that provided us with built-in functions to manipulate arrays and dataframes. Although this can be done in C++, it would have been significantly more labour/time intensive.

#### 4. Would it be better to have the server poll the sensors, or the sensors to reach out to the server when they have data?
Having the servers poll the sensors is beneficial if you want a constant stream of real-time data. This would be important in scenarios where you have to actively monitor information being gathered from the sensors (ie: monitoring incubation temperatures). For the purposes of our assignment, this was helpful because we constantly received data so it would make sense for the server to constantly pull that data from the sensor. It would be better for the sensors to reach out to the server when they have data if the data stream was significantly more delayed. This would reduce the amount of power you would need to have the server constantly on and reduces idle time.
