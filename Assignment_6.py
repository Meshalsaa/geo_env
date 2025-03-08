import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tools
# Open the dataset
dset = xr.open_dataset(r'C:\Users\Mesha\Downloads\download.nc')

# Exctract temp, precipitation, lat, long, and time
t2m = np.array(dset.variables['t2m'])
tp = np.array(dset.variables['tp'])
latitude = np.array(dset.variables['latitude'])
longitude = np.array(dset.variables['longitude'])
time_dt = np.array(dset.variables['time'])

#Convert temp from K to C and precipitation from m h−1 to mm h−1 
t2m = t2m-273.15
tp = tp * 1000

# Simplify the data by computing the mean acroos the second dimension, IF the data is four dimesional

if t2m.ndim == 4:
    t2m = np.nanmean(t2m, axis=1)
    tp = np.nanmean(tp, axis=1)
    
# Creating a pandas dataframe of time series for both temp and rain. Focus on the grid cell closest to the reservoir (row 3, column 2):
df_era5 = pd.DataFrame(index=time_dt)
df_era5['t2m'] = t2m[:, 3, 2]
df_era5['tp'] = tp [:, 3, 2]

# Then Plot
df_era5.plot()
plt.show()

# Resample the data to annual time step and calculate the mean percipitation
annual_percip = df_era5['tp'].resample("YE").mean()*24*365.25
mean_annual_percip = np.nanmean(annual_percip)
print(mean_annual_percip)               # The mean Annual Average is 88.34

# Calculation of potential evaporation
tmin = df_era5['t2m'].resample('D').min().values
tmax = df_era5['t2m'].resample('D').max().values
tmean = df_era5['t2m'].resample('D').mean().values
lat = 21.5
doy = df_era5['t2m'].resample('D').mean().index.dayofyear

# Compute the PE using tools:
pe = tools.hargreaves_samani_1982(tmin, tmax, tmean, lat, doy)

# Plot the PE series
ts_index = df_era5['t2m'].resample('D').mean().index
plt.figure()
plt.plot(ts_index, pe, label = 'Potential Evaporation')
plt.xlabel('Time')
plt.ylabel("Potential evaporation (mm d-1)")
plt.show()

# Mean Annual PE
mean_annual_PE = np.nanmean(pe) * 365 
print(f"Mean Annual PE: {mean_annual_PE} mm y−1")