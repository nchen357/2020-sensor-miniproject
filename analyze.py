#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np


def load_data(file: Path) -> T.Dict[str, pandas.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {
        "temperature": pandas.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pandas.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pandas.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()
    #load our data
    data = load_data(file)
    timeInterval = []
    #Iterate through each line in data
    for k in data:
        # data[k].plot()
        #Only do this when we're at temperature or occupancy
        if k == "temperature" or k == "occupancy":
            data_title = "class1: " +  k[0].upper() + k[1:] + " Data"
            print(data_title)
            #Find median and variance of data for temperature or occupancy
            print("Median:", str(data[k]['class1'].median()))
            print("Variance:", str(data[k]['class1'].var()))
        #data[k].hist()
        #plt.figure()
        #plt.hist(np.diff(time.values).astype(np.int64) // 1000000000)
        #plt.xlabel("Time (seconds)")
        plt.figure()
        data[k]['class1'].plot.density()
        plt.title("Probability Density Function of class 1: " + k)


        if k == 'temperature':
            plt.xlabel("Temperature")
        elif k == "occupancy":
            plt.xlabel("Occupancy")
        else:
            plt.xlabel("Units")

    #Providing indicies to our dataframe
    print(type(data["temperature"]))
    time = data["temperature"].index
    print(time[0])
    print(type(time))
    #print(data["temperature"])
    #print(time)

    #find difference in the time so we can plot it
    timeDifference = time[1:] - time[:-1]
    #print(timeDifference)

    #Finding the total duration of each element in just seconds
    for t in timeDifference:
        timeInterval.append(t.total_seconds())
    #Create a 1-D array so we are able to graph it
    timeSeries = pandas.Series(timeInterval)
    #print(timeSeries)

    #Print out our stats
    print("Time Interval Stats")
    #Finding the mean and variance of the time interval of the sensor reading
    print('Mean: ' + str(timeSeries.mean()))
    print('Variance: ' + str(timeSeries.var()))

    #normal distribution...? :D



    plt.figure()
    #Plot our time interval probability density function
    timeSeries.plot.density()
    plt.title("Time Interval Probability Density Function")
    plt.xlabel("Time (sec)")
    plt.show()
