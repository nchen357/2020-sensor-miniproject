#This program detects anomalies in temperature sensor data
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


    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}


    data = pandas.DataFrame.from_dict(temperature, "index").sort_index(),


    return data

def detection(data):
    name = 'class1'
    classData = data[0][name]
    #Discard the bad data aka the NAs
    classData = classData.dropna()
    #Find the mean and standard deviation of classData
    meanData = classData.mean()
    stdData = classData.std()
    print("Values for Original Data")
    print("Mean of Class1 data:", str(meanData))
    print("Variance of Class1 data:", str(stdData**2))


    #Filtering the bad data by removing things 2 standard deviations above and below
    goodData = classData[(classData <= (meanData + 2*stdData)) & (classData >= (meanData - 2*stdData))]
    #Finding the median and variance of the filtered data
    goodMedian = goodData.median()
    goodVar = goodData.var()
    print("Mean of readjusted Class1 data:", str(goodMedian))
    print("Variance of readjusted Class1 data:", str(goodVar))
    print("Percentage of total data points that have been excluded: ", str(100-len(goodData)/len(classData)*100))
    return goodData


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()
    #load our data
    data = load_data(file)
    goodData = detection(data)
    plt.figure()
    goodData.plot.density()
    plt.title("Probability Density Function of class 1 temperature (excluded values)")
    plt.xlabel("Temperature")
    plt.show()
