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
# # Session 3

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
with open("data/pulse_data.csv", "r") as f:
    next(f)  # skip header

    for line in f:
        t, p = line.strip().split(",")
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
