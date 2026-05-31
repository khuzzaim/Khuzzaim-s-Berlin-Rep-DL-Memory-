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

# %% [markdown]
# # Session 8

# %%
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: '1.16.0'
# ---

# %%
# Importing Program
from spacemed.fmri import (
    normalize,
    compute_slice_activation,
)
# %%
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib

# %%
# %%
import os
print(os.getcwd())

# %%
# %%
import os
print(os.listdir())

# %%
# %%
import tarfile

with tarfile.open("fmri-data.tar.gz") as tar:
    for name in tar.getnames():
        print(name)

# %%
# %%
with tarfile.open("fmri-data.tar.gz") as tar:
    tar.extractall()

# %%
# %%
import os

print(os.listdir())

# %%
# %%
print(os.listdir("fmri-data"))

# %%
# %%
fmri = nib.load("fmri-data/3_fMRI_TR2sec_3mm_3min.nii")
print(fmri.shape)

# %%
# Coverting to NumPy array
# %%
data = fmri.get_fdata()

print(data.shape)

# %%
# Visualizing brain slices
# %%
plt.imshow(data[30, :, :, 0].T, cmap="gray", origin="lower")
plt.title("Brain Slice")
plt.colorbar()
plt.show()

# %%
print(data.shape)

# %%
x = data.shape[0] // 2
y = data.shape[1] // 2
z = data.shape[2] // 2

plt.imshow(data[x, :, :, 0].T, cmap="gray", origin="lower")
plt.title("Middle Slice")
plt.show()

# %%
# %%
x_mid = data.shape[0] // 2
y_mid = data.shape[1] // 2
z_mid = data.shape[2] // 2
t = 0  # first time point

print(data.shape)

# %%
# Saggital plane
# %%
plt.imshow(data[x_mid, :, :, t].T, cmap="gray", origin="lower")
plt.title("Sagittal Plane (side view)")
plt.xlabel("Y")
plt.ylabel("Z")
plt.colorbar()
plt.show()

# %%
# Coronal Plane
# %%
plt.imshow(data[:, y_mid, :, t].T, cmap="gray", origin="lower")
plt.title("Coronal Plane (front view)")
plt.xlabel("X")
plt.ylabel("Z")
plt.colorbar()
plt.show()

# %%
# Transverse Plane
# %%
plt.imshow(data[:, :, z_mid, t].T, cmap="gray", origin="lower")
plt.title("Transverse Plane (top view)")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar()
plt.show()

# %%
# %%
import os

for root, dirs, files in os.walk("."):
    if "ols.csv" in files:
        print("FOUND:", os.path.join(root, "ols.csv"))

# %%
# Loading CSV file
# %%
import pandas as pd

ols = pd.read_csv("./data/ols.csv", index_col="Vehicle")
print(ols.head())

# %%
# %%
import sys
print(sys.executable)

# %%
# Importing Seaborn
# %%
import seaborn as sns

# %%
# Linear Correlation
# %%
sns.regplot(
    data=ols,
    x="Initial Mass (kg)",
    y="Payload Mass to LEO (kg)",
    order=1
)

# %%
# Non-linear Correlation
# %%
sns.regplot(
    data=ols,
    x="Length (m)",
    y="Payload Mass to LEO (kg)",
    order=2
)

# %%
# Time Series
## Building Time Axis
# %%
nt = fmri.shape[-1]
sampling_rate = fmri.header.get_zooms()[-1]

times = np.arange(nt) * sampling_rate

# %%
# Picking meaningful voxels
# %%
voxel_1 = (19, 24, 25)
voxel_2 = (19, 25, 25)
voxel_3 = (40, 25, 25)

# %%
# Extracting time series
# %%
sig1 = data[voxel_1]
sig2 = data[voxel_2]
sig3 = data[voxel_3]

print(sig1.shape)  # should be (nt,)

# %%
# Plotting time series raw signal
# %%
plt.plot(times, sig1, label="Voxel 1")
plt.plot(times, sig2, label="Voxel 2")
plt.plot(times, sig3, label="Voxel 3")

plt.xlabel("Time (s)")
plt.ylabel("Signal")
plt.title("Raw fMRI Signals")
plt.legend()
plt.show()

# %%
# Defining Signals
# %%
sig1_n = normalize(sig1)
sig2_n = normalize(sig2)
sig3_n = normalize(sig3)

# %%
# Plotting Normalized
# %%
plt.plot(times, sig1_n, label="Voxel 1")
plt.plot(times, sig2_n, label="Voxel 2")
plt.plot(times, sig3_n, label="Voxel 3")

plt.xlabel("Time (s)")
plt.ylabel("Normalized Signal")
plt.title("Normalized Signals")
plt.legend()
plt.show()

# %%
# Spectral Analysis
## Priodogram
# %%
from scipy import signal as sg

freq1, power1 = sg.periodogram(sig1_n, fs=1/sampling_rate)
freq2, power2 = sg.periodogram(sig2_n, fs=1/sampling_rate)
freq3, power3 = sg.periodogram(sig3_n, fs=1/sampling_rate)

# %%
# Plotting 
# %%
plt.plot(freq1, power1, label="Voxel 1")
plt.plot(freq2, power2, label="Voxel 2")
plt.plot(freq3, power3, label="Voxel 3")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.title("Periodograms")
plt.legend()
plt.show()

# %%
# Building Stimulus Signal
# %%
sone = np.array([1]*5 + [0]*5)

signal_input = np.tile(sone, int(np.ceil(nt / len(sone))))
signal_input = signal_input[:nt]

signal_input_n = normalize(signal_input)

# %%
# Cross Correlation
# %%
cross1 = sg.correlate(sig1_n, signal_input_n, mode="same")
cross2 = sg.correlate(sig2_n, signal_input_n, mode="same")
cross3 = sg.correlate(sig3_n, signal_input_n, mode="same")

lags = sg.correlation_lags(len(sig1_n), len(signal_input_n), mode="same")

# %%
# Plotting Correlation
# %%
plt.plot(lags, cross1, label="Voxel 1")
plt.plot(lags, cross2, label="Voxel 2")
plt.plot(lags, cross3, label="Voxel 3")

plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.title("Cross-Correlation")
plt.legend()
plt.show()

# %%
# Finding Best Lag
# %%
print("Voxel 1 lag:", lags[np.argmax(cross1)])
print("Voxel 2 lag:", lags[np.argmax(cross2)])
print("Voxel 3 lag:", lags[np.argmax(cross3)])

# %%
# Choosing a slice
# %%
z = data.shape[2] // 2   # middle slice

# %%
# Creating an empty result map
# %%
slice_shape = data.shape[:2]
activation_map = np.zeros(slice_shape)

# %%
# Looping over all voxels
# %%
signal_input_n = normalize(signal_input)

for x in range(data.shape[0]):
    for y in range(data.shape[1]):

        voxel_signal = data[x, y, z]

        if np.std(voxel_signal) == 0:
            continue

        voxel_signal_n = normalize(voxel_signal)

        cross = sg.correlate(voxel_signal_n, signal_input_n, mode="same")

        activation_map[x, y] = np.max(cross)

# %%
# Filtering
# %%
from scipy.ndimage import gaussian_filter

activation_smooth = gaussian_filter(activation_map, sigma=1)

# Clipping weak signals
# %%
threshold = np.percentile(activation_smooth, 90)
activation_thresh = np.where(activation_smooth > threshold, activation_smooth, 0)

# %%
# Visualising activation map
# %%
plt.imshow(activation_thresh.T, cmap="hot", origin="lower")
plt.colorbar()
plt.title("Activation Map")
plt.show()
