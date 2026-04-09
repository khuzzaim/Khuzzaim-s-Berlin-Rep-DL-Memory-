# Session 3 – Loading Data with Python

## Overview
In this session, we learned how to load and work with data using Python. The focus was on reading data from files and visualizing it.

## Data and Metadata
Data refers to the actual values (e.g., pulse measurements), while metadata provides additional information about the data (e.g., labels such as time and pulse).

## Getting Data
We extracted the dataset from a compressed archive using:
tar xvf session3-data.tar.gz

This created a data directory containing the file pulse_data.csv.

## Loading Data with Python
We loaded the data from the CSV file by opening the file and reading it line by line. The first line (header) was skipped, and the remaining data was split into two columns.

Each value was converted from a string to a float and stored in separate lists for time and pulse.

## Plotting Data
We used matplotlib to plot the pulse data over time. The time values were used for the x-axis and the pulse values for the y-axis.

## Conclusion
This session introduced how to load data from files, process it in Python, and visualize it using plots.
