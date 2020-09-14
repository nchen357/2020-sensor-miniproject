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
    print("Standard Deviation of Class1 data:", str(stdData))
    print(classData)

    #Find anomalies in the data
    badData = classData[(classData >= (meanData + stdData)) | (classData <= (meanData - stdData))]
    badMean = badData.mean()
    badStd = badData.std()
    print("Mean of excluded Class1 data:", str(badMean))
    print("Standard Deviation of excluded Class1 data:", str(badStd))
    print("Percentage of total data points excluded: ", str(len(badData)/len(classData)*100))
    print(badData)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()
    #load our data
    data = load_data(file)
    detection(data)
