# Session 3 – Loading Data with Python

## Overview
In this session, we learned how to work with data using the Unix shell and Python. The main focus was on loading, processing, and visualizing data.

## Data and Metadata
Data refers to the actual values (e.g., pulse measurements), while metadata provides information about the data (e.g., time, units, or descriptions). Metadata is important for understanding and organizing datasets.

## Getting Data
We extracted data from a compressed file using:
tar xvf session3-data.tar.gz

We also explored downloading datasets using wget and extracting them with unzip.

## Shell Commands
We used several useful shell commands:
- wc: count lines/words
- du: check disk usage
- head/tail: preview files
- grep: search inside files
- find: locate files

## Loading Data with Python
We used NumPy to load data from a CSV file:
np.loadtxt("data/pulse_data.csv", delimiter=",", skiprows=1)

This allowed us to efficiently read numerical data into arrays.

## Plotting Data
We used Matplotlib to visualize the data:
plt.plot(time, pulse)

This produced a graph showing how pulse changes over time.

## Conclusion
This session introduced the full workflow of handling data: extracting, inspecting, loading, and visualizing it using Python tools.
