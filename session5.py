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
# # Session 5: Python Modules and Pandas

# %%
## Loading and Exploring Data

# %%
import pandas
# %pwd
# %cd mukh11

# %%
station_ids = pandas.read_csv("data/Niederschlag_1981-2010_Stationsliste.txt", encoding="iso-8859-1", delimiter=" *; *", engine="python")

# %%
station_ids

# %%
station_ids.columns

# %%
station_ids.info()

# %%
station_ids.head()

# %%
station_ids.tail()

# %%
station_ids.columns

# %%
station_ids.info()

# %%
station_ids.head()

# %%
station_ids.columns

# %%
station_ids.drop(columns=["Unnamed: 6"], inplace=True)

# %%
station_ids = station_ids.set_index("Stations_id")

# %%
station_ids.columns

# %%
station_ids["Bundesland"]

# %%
station_ids.groupby("Bundesland").count().sort_values("Stationsname", ascending=False)

# %%
mask = station_ids.Bundesland == "Bayern"

# %%
mask

# %%
station_ids[mask]

# %%
bayern = station_ids[mask]

# %%
station_ids.Bundesland.iloc[-1]

# %%
bayern.loc[17]

# %%
mask = station_ids.Bundesland == "Berlin"

# %%
berlin = station_ids[mask]
berlin

# %%
berlin["Stationsname"]

# %%
berlin[berlin["Stationsname"].str.contains("Alexander")]

# %%
precip = pandas.read_csv(
    "data/produkt_precipitation_399_akt.txt",
    delimiter=" *; *",
    engine="python"
)

# %%
precip.head()
precip.columns

# %%
precip.MESS_DATUM = pandas.to_datetime(
    precip.MESS_DATUM,
    format="%Y%m%d%H"
)

# %%
precip = precip[["MESS_DATUM", "NIEDERSCHLAGSHOEHE"]]

precip = precip.rename(columns={
    "MESS_DATUM": "date",
    "NIEDERSCHLAGSHOEHE": "precipitation"
})

precip = precip.set_index("date")

# %%
monthly = precip.resample("ME").sum()

# %%
monthly.head()
monthly.describe()

# %%
precip_ref = pandas.read_csv(
    "data/Niederschlag_1981-2010.txt",
    delimiter=" *; *",
    encoding="iso-8859-1",
    engine="python",
    decimal=","
)

# %%
berlin[berlin["Stationsname"].str.contains("Alexander", case=False)]

# %%
station_id = 399

# %%
precip_ref.head()

# %%
precip_ref.columns

# %%
precip_ref.loc[station_id]

# %%
precip_ref

# %%
precip_ref.drop(precip_ref.columns[-1],axis=1, inplace=True)

# %%
precip_ref

# %%
precip_ref=precip_ref.loc[:, "Jan.":"Dez."]

# %%
precip_ref.loc[station_id].plot.bar()

# %%
precip = pandas.read_csv(
    "data/produkt_precipitation_399_akt.txt",
    delimiter=" *; *",
    engine="python"
)

# %%
precip.head()
precip.columns

# %%
precip["MESS_DATUM"] = pandas.to_datetime(
    precip["MESS_DATUM"],
    format="%Y%m%d%H"
)

# %%
precip.head()

# %%
precip = precip[["MESS_DATUM", "NIEDERSCHLAGSHOEHE"]]

# %%
precip = precip.rename(columns={
    "MESS_DATUM": "date",
    "NIEDERSCHLAGSHOEHE": "precipitation"
})

# %%
precip = precip.set_index("date")

# %%
monthly = precip.resample("ME").sum()

# %%
monthly.head()

# %%
refs = pandas.DataFrame(
    {"precipitation": precip_ref.loc[station_id].to_list() * 11},
    index=pandas.date_range("2015-01-01", "2025-12-31", freq="ME")
)

# %%
monthly["climate"] = refs

# %%
monthly["anomaly"] = monthly["precipitation"] - monthly["climate"]

# %%
monthly[["precipitation", "climate"]].plot()

# %%
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10,6))

monthly[["precipitation", "climate"]].plot(ax=ax)

ax.set_title("Precipitation Berlin (Alexanderplatz)")

# %%
monthly["anomaly"].plot()

# %%
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3, 1, figsize=(12,10))

# Actual vs Climate
monthly[["precipitation", "climate"]].plot(ax=axs[0])
axs[0].set_title("Actual vs Climate Precipitation")
axs[0].set_ylabel("mm")

# Anomaly line plot
monthly["anomaly"].plot(ax=axs[1])
axs[1].set_title("Precipitation Anomaly")
axs[1].set_ylabel("mm")

# Anomaly bar plot 
monthly["anomaly"].plot(kind="bar", ax=axs[2])

for i, label in enumerate(axs[2].get_xticklabels()):
    if i % 12 != 0:
        label.set_visible(False)

axs[2].set_title("Anomaly Bar Plot")
axs[2].set_ylabel("mm")

# show only yearly labels
ax.set_xticks(range(0, len(monthly), 12))
ax.set_xticklabels(monthly.index.strftime("%Y")[::12], rotation=45)

axs[2].set_title("Anomaly Bar Plot")
axs[2].set_ylabel("mm")

plt.tight_layout()
# %%

