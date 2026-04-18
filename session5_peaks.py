# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python [conda env:.conda-spacemed]
#     language: python
#     name: conda-env-.conda-spacemed-py
# ---

# # Session 5 Peaks

import jupytext

# +
# Imports
# -

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# +
# Load data

# +
# Load pulse data
data = pd.read_csv("data/pulse_data.csv")

# Preview data
data.head()

# +
# Plot Signal
# -

# Plot absorption signal
plt.plot(data.absorption)
plt.title("Pulse Signal")
plt.xlabel("Time")
plt.ylabel("Absorption")
plt.show()

# +
# Peak Detection

# +
# Detect all peaks (includes noise)
peaks, properties = find_peaks(data.absorption)

len(peaks)

# Without constraints, find_peaks detects all local maxima,
# including noise and small fluctuations

# +
# Fix: Filter Peaks
# -

# Detect meaningful peaks using filtering
peaks, properties = find_peaks(
    data.absorption,
    height=2800,
    distance=120
)

# +
# Plot with peaks

plt.figure(figsize=(10,5))
plt.plot(data.absorption)
plt.scatter(peaks, data.absorption.iloc[peaks])
plt.title(f"Filtered Peaks (Total: {len(peaks)})")
plt.show()
# -

data.absorption.describe()

# +
# The absorption signal ranges from ~1000 to ~3600. 
# Initial peak detection resulted in 401 peaks due to the absence of filtering. 
# By setting a height threshold around 2500 and enforcing a minimum distance between peaks, 
# we successfully removed noise and retained physiologically meaningful peaks.
