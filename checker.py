#!/usr/bin/env python3.7
"""
This program double checks our values for temperature to make sure our numbers are correct for the graph -> NOT PART OF THE ASSIGNMENT.
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


    for k in data:
        if k == "temperature":
            normalData = data[k]['class1'].dropna()
    #finding out our maximum
    print("Max: ", str(max(normalData)))
    print("Min: ", str(min(normalData)))
    #Find mean and standard deviation for Filtering
    meanData = normalData.mean()
    stdData = normalData.std()

    #upper boundary and lower boundary
    upperBound = meanData + (stdData*2)
    lowerBound = meanData - (stdData*2)
    filterIndex = []
    for i in range(len(normalData)):
        if lowerBound <= normalData[i] <= upperBound:
            filterIndex.append(i)
    filteredData = normalData[filterIndex]

    #Check to see how many points we removed after filtered
    lenNorm = len(normalData)
    lenFilter = len(filteredData)
    print("Length of normal data: ", str(lenNorm))
    print("Length of filtered data: ", str(lenFilter))
    print("Percentage of removed data: ", str(lenFilter/lenNorm))
    print("Filtered Max: ", str(max(filteredData)))
    print("Filtered Min: ", str(min(filteredData)))
