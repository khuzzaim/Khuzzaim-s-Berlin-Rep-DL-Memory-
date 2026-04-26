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
#     display_name: Python [conda env:.conda-spacemed]
#     language: python
#     name: conda-env-.conda-spacemed-py
# ---

# %%
# # %load_ext autoreload
# # %autoreload 2

# %%
import spacemed
import matplotlib.pyplot as plt

# %%
spacemed.__version__

# %%
# Load data
time, absorption = spacemed.read_pulse("../data/pulse_data.csv")

# %%
# Plot signal
plt.plot(time, absorption)
plt.xlabel("Time")
plt.ylabel("Absorption")
plt.title("Absorption over Time")
plt.show()

# %%
# Use package function
peaks = spacemed.find_peaks(time, absorption)

# %%
print("Number of peaks detected:", len(peaks))

# %%
# Heart rate calculation
heart_rate = spacemed.calc_heart_rate(time, peaks)

# %%
# Plot heart rate
plt.plot(peaks[1:], heart_rate)
plt.xlabel("time [s]")
plt.ylabel("heart rate [bpm]")
plt.show()
