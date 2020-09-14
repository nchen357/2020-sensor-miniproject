---
<p align = "center"><b>Memorandum</b></p>

---

**TO:** EC463 Professors

**FROM:** EC463 Students Nicole Chen and Ye Chen

**SUBJECT:** 2020 Sensor Miniproject

**DATE:** September 17, 2020

**PURPOSE**
	The goal of this memo is to report our findings and methodologies in programming the sensor algorithms as well as answer any conceptual questions posed throughout the project.

**DISCUSSION**
**Part One: Data flow**
	The 2020 Sensor Miniproject is a python based project that utilizes IoT simulators to simulate data; Upon activating the IoT simulators, we were met with the following message:
> ECE Senior Capstone IoT Simulator

**Part Two: Analysis**
After confirming the IoT simulators functions, we proceeded to save the outputted data into a data.json file, wrote a script to analyze the data and found various measurements for a specific room of our choice - class 1. We have included the specific data set we are analyzing in this repository. Our measurements are as follows:

> Temperature Data
* Median: 26.99
* Variance: 13213.42
> Occupancy Data
* Median: 19.0
* Variance: 19.52
> Time Interval Stats
* Mean: 6.85
* Variance: 223920.55

	Our recorded probability functions for various parameters:
![image](https://i.imgur.com/W1uYFId.png)
![image](https://i.imgur.com/vg4a1DZ.png)
![image](https://i.imgur.com/h9jRPmr.png)
![image](https://i.imgur.com/MjbM7mq.png)


There is *some* normal distribution within the sensor data, much akin to larger systems, but it is dramatically skewed by extreme values as indicated by the enormous variance.

**Part Three: Design**
This tuning is performed via our script, anomaly.py, where only data points that are within 2 standard deviations of the average are included. We decided to implement this algorithm because it was sufficient enough to eliminate our outliers without being too strict and eliminating too much of our data points. From these parameters, the measurements are ran again for class 1.

> Readjusted Temperature Data
* Median: 24.64
* Variance: 50.47
* Percentage of total data that has been excluded: 0.088%


The readjusted data is far more consistent and it appears to prove that less than 5% of the data is drastically skewing the distribution. Stray and extreme values such as these should be rightfully removed to get properly tuned data. If these extreme data points were more persistent and constituted a larger percentage of the data (upwards of 5% and over), then it could possibly indicate a failed or failing sensor. From these findings, we can conclude that at least 2 standard deviations from the mean would be a feasible bounds on temperature. In Class 1's case, this bound would be from 1.91 to 52.39 degrees.

**Part four: Conclusion**

The simulation does appear to be reflective of the real world - with so many physical and sometimes unpredictable variables, sensors in the real world also tend to have drastic but momentary changes in temperature. The amount of these spikes is typically very low and can be easily tuned out, just as we have observed with the simulated sensors where we used our filtering algorithm to remove any outliers. Overall our data was very consistent which is realistic given that we are gathering information from a singular room that most likely does not have that many environmental changes. This simulation does have a few drawbacks however, and without real world parameters there can only be so much these sensors can emulate with proper accuracy. The random number generation for formulating the sensor data may either not be accurate enough or could possibly be even too predictable in comparison with the real world. In a more realistic simulation of the real world, there would be times where our temperature would increase or decrease due to changes in the weather but ours remains relatively constant. Our lack of hardware components also means that while our software simulation is interesting, it leaves us unable to account for any skew in our data caused by deviation in physical variables which would make testing potentially inaccurate during a field test.
On the software side, however, the Python coding has been smooth and overall the websockets library is quite convenient.  
