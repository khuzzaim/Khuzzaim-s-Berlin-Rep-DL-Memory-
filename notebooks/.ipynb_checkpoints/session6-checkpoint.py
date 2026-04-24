# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python [conda env:conda_envs-gpulab]
#     language: python
#     name: conda-env-conda_envs-gpulab-py
# ---

# %% [markdown]
# # Session 6: Modding Session 4's Heart Rate Analysis

# %%
# Importing Functions

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# Naming empty lists

# %%
time = []
absorption = []

# %%
# Load absorption data from CSV file

# %%
with open('../data/pulse_data.csv', 'r') as f:
    next(f)
    
    for line in f:
        t, p = line.strip().split(',')
        time.append(float(t))
        absorption.append(float(p))

# %%
# Convert to numpy

# %%
time = np.array(time)
absorption = np.array(absorption)

# %%
# Plot pulse data over time using matplotlib

# %%
plt.plot(time, absorption)
plt.xlabel("Time")
plt.ylabel("Absorption")
plt.title("Absorption over Time")
plt.show()

# %%
# Peak Detection

##Peaks correspond to heart beats and are identified as local maxima in the absorption signal.

##Using NumPy arrays allows efficient vectorized comparison of neighboring values to detect peaks.

##A minimum time separation between consecutive peaks is enforced to ensure that detected peaks represent physiological heart beats rather than noise.

# %%
peak_indices = np.where(
    (absorption[1:-1] > absorption[:-2]) &
    (absorption[1:-1] > absorption[2:])
)[0] + 1

# %%
# Applying Time Separation

# %%
peaks = time[peak_indices]

filtered_peaks = [peaks[0]]

for t in peaks[1:]:
    if t - filtered_peaks[-1] > 0.3:
        filtered_peaks.append(t)

peaks = np.array(filtered_peaks)

# %%
print(len(peaks))

# %%
print("Number of peaks detected:", len(peaks))

# %%
# Time Difference Between Peaks

# We compute the time difference between consecutive peaks.

# %%
delta_t = np.diff(peaks)

# %%
# Heart Rate Calculation

#The heart rate is calculated using:

# H = 60 / ΔT

# where ΔT is the time between peaks.

# %%
heart_rate = 60 / delta_t

# %%
# Heart Rate Plot

# We plot the heart rate over time.

# %%
plt.plot(peaks[1:], heart_rate)
plt.xlabel("time [s]")
plt.ylabel("heart rate [bpm]")
plt.show()

# %% [raw]
# # Result and Discussion
#
# The computed heart rate varies over time and reflects the physiological changes in the signal.
#
# The values obtained are within a realistic range for heart rate measurements.

# %% [raw]
# # Conclusion
#
# In this session, we:
# - visualized the absorption signal
# - identified peaks corresponding to heart beats
# - computed time intervals between peaks
# - calculated the heart rate
# - visualized the heart rate over time
#
# This demonstrates basic algorithm design applied to physiological data.
