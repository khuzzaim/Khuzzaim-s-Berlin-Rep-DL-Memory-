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
# # Session 4: Heart Rate Analysis

# %%
# Load absorption data from CSV file
# Skip header and convert values to float

# %%
# Extract time and pulse values

# %%
time = []
absorption = []

# %%
# Extract time and pulse values

# %%
with open('data/pulse_data.csv', 'r') as f:
    next(f)  # skip header
    
    for line in f:
        t, p = line.strip().split(',')
        time.append(float(t))
        absorption.append(float(p))

# %%
# Load pulse data from csv file

# %%
from matplotlib import pyplot as plt

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

# A peak is defined as a point that is higher than its neighboring values.

# These peaks correspond to heart beats.

# %%
peaks = []

for i in range(1, len(absorption)-1):
    if absorption[i] > absorption[i-1] and absorption[i] > absorption[i+1]:
        if len(peaks) == 0 or (time[i] - peaks[-1]) > 0.5:
            peaks.append(time[i])

# %%
print(len(peaks))

# %%
# Time Difference Between Peaks

# We compute the time difference between consecutive peaks.

# %%
delta_t = []

for i in range(1, len(peaks)):
    diff = peaks[i] - peaks[i-1]
    delta_t.append(diff)

# %%
# Heart Rate Calculation

#The heart rate is calculated using:

# H = 60 / ΔT

# where ΔT is the time between peaks.

# %%
heart_rate = []

for dt in delta_t:
    hr = 60 / dt
    heart_rate.append(hr)

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
