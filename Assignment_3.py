import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr
import tools

# Visualizing the data
df_isd = tools.read_isd_csv(r"C:\Users\Mesha\Downloads\41024099999.csv")
plot = df_isd.plot(title = "ISD data for Jeddah")
plt.show()

# Converting dewpoint temperature (C) to relative humidity(%)
# Adding a new column for RH (relative humidity)
df_isd['RH'] = tools.dewpoint_to_rh(df_isd['DEW'].values, df_isd['TMP'].values)
print(df_isd)

# Calculating HI from air temperature and relative humidity
df_isd['HI'] = tools.gen_heat_index(df_isd['TMP'].values, df_isd['RH'].values)
print(df_isd)

# The highest HI observed in the year
print(df_isd.max())

# Day and Time where HI is highest
print(df_isd.idxmax())

# What air temperature and relative humidity were observed at this moment?
print(df_isd.loc[["2024-08-10 11:00:00"]])
df_daily = df_isd.resample('D').agg({'TMP': 'max', 'RH': 'mean', 'HI': 'max'})  # Daily resampling
print(df_daily)

# Resample to daily data by taking the mean HI per day
df_daily = df_isd.resample('D').mean()

# Plot Heat Index (HI) time series (Daily)
plt.figure(figsize=(12, 6))
plt.plot(df_daily.index, df_daily['HI'], label='Daily Heat Index (HI)', color='red', linewidth=1)

# Formatting
plt.xlabel('Date')
plt.ylabel('Heat Index (°C)')
plt.title('Daily Heat Index (HI) Time Series for the Year')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Save the figure
plt.savefig("HI_daily_timeseries.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()

#Open the ssp245 dataset
ssp245_dset = xr.open_dataset(r"C:\Users\Mesha\geo_env course data\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc")

# Selcet the air temperature column
tas = ssp245_dset['tas']

# Extract the data (coordinates) for jeddah 
tas_jeddah_ssp245 = tas.sel(lat = 21.4, lon = 39.1, method = "nearest")

# Convert to Celcius
tas_jeddah_ssp245 = tas_jeddah_ssp245 - 273.15

# Visualize the data
print(tas_jeddah_ssp245)

# Calculate the average temperature for ssp245 scenario
tas_jeddah_ssp245_mean = tas_jeddah_ssp245.sel(time=slice("2071", "2100")).mean().values

# Calculate the average temperature for ssp245 scenario
df_isd_mean = df_isd['TMP'].mean()

# Calculate the projeccted warming 
projected_warming = df_isd_mean - tas_jeddah_ssp245_mean
print(projected_warming)

# Apply warming to observed temperature
df_isd['TMP_future'] = df_isd['TMP'] + projected_warming

# Recalculate HI with the adjusted temperature
df_isd['HI_future'] = tools.gen_heat_index(df_isd['TMP_future'].values, df_isd['RH'].values)

# Compare max HI after warming
max_HI_after = df_isd['HI_future'].max()
max_HI_jeddah = df_isd['HI'].max()
HI_increase = max_HI_after - max_HI_jeddah
print(HI_increase)
