---
<p align = "center">#**Memorandum**</p>
---
**TO:** EC463 Professors
**FROM:** EC463 Students Nicole Chen and Ye Chen
**SUBJECT:** 2020 Sensor Miniproject 
**DATE:** September 17, 2020
---
##**Purpose**
	The goal of this memo is to report our findings and methodologies in programming the sensor algorithms as well as answer any conceptual questions posed throughout the project.

##**Discussion**
	The 2020 Sensor Miniproject is a python based project that utilizes IoT simulators to simulate data; Upon activating the IoT simulators, we were met with the following message:
> ECE Senior Capstone IoT Simulator

	After confirming the IoT simulators functions, we proceeded to save the outputted data into a data.json file, wrote a script to analyze the data and found various measurements for a specific room of our choice - class 1. We have included the specific data set we are analyzing in this repository. Our measurements are as follows:
<p align = "center">
> Temperature Data
* Median: 26.99
* Variance: 13213.42
> Occupancy Data
* Median: 19.0
* Variance: 19.52
> Time Interval Stats
* Mean: 6.85
* Variance: 223920.55
</p>
	Our recorded probability functions for various parameters:
![image]
![image]
![image]
![image]

	There is *some* normal distribution within the sensor data, much akin to larger systems, but it is dramatically skewed by extreme values as indicated by the enormous variance. 

	This tuning is performed via our script, anomaly.py, where only data points that are within 2 standard deviations of the average are included. From these parameters, the measurements are ran again for class 1.
<p align = "center">
> Readjusted Temperature Data
* Median: 24.64
* Variance: 50.47
* Percentage of total data that has been excluded: 0.088%
</p>

	The readjusted data is far more consistent and it appears to prove that less than 5% of the data is drastically skewing the distribution. Stray and extreme values such as these should be rightfully removed to get properly tuned data. If these extreme data points were more persistent and constituted a larger percentage of the data (upwards of 5% and over), then it could possibly indicate a failed or failing sensor. From these findings, we can conclude that at least 2 standard deviations from the mean would be a feasible bounds on temperature. In Class 1's case, this bound would be from 1.91 to 52.39 degrees. 

**Conclusion**
	The simulation does appear to be reflective of the real world - with so many physical and sometimes unpredictable variables, sensors in the real world also tend to have drastic but momentary changes in temperature. The amount of these spikes is typically very low and can be easily tuned out, just as we have observed with the simulated sensors. This simulation does have a few drawbacks however, and without real world parameters there can only be so much these sensors can emulate with proper accuracy. The random number generation for formulating the sensor data may either not be accurate enough or could possibly be even too predictable in comparison with the real world. Our lack of physical components also means that while testing the software is interesting, we will absolutely be unable to account for any skew in our data caused by deviation in physical variables and thus results may greatly vary when a field test is performed. On the software side, however, the Python coding has been smooth and overall the websockets library is quite convenient.  





