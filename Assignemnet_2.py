import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr

# Visualizing and inspecting the data 

# Import the data
dset = xr.open_dataset(r"C:\Users\Mesha\geo_env course data\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_195001-201412.nc")

# Check the dataset
print(dset)

#Breakpoint
pdb.set_trace()

# Inspect the dataset
print(dset.keys())

#Break point
pdb.set_trace()

# Access the air temperature variable
tas = dset['tas']

# Print the dimensions of the air temperature variable
print(tas.dims)

# The Air Temperature data type
print(tas.dtype)

# Break point
pdb.set_trace()

# Calculation and visualization of different climate change scenarios compared to the pre-industrial period.

# Pre-industrial Period
pre_industrial_dset = xr.open_dataset(r"C:\Users\Mesha\geo_env course data\Climate_Model_Data\tas_Amon_GFDL-ESM4_historical_r1i1p1f1_gr1_185001-194912.nc")

# Calculate the mean temperature for 1850–1900
mean_1850_1900 = np.mean(pre_industrial_dset['tas'].sel(time=slice('1850-01-01', '1900-12-31')), axis=0)

# Convert to Numpy array
mean_1850_1900 = np.array(mean_1850_1900)

#Convert to Celsius
mean_1850_1900 = mean_1850_1900 - 273.15 # Pre-industrial temperature in Celsius

# Check the shape and dtype of the result
print("Pre-industrial shape:", mean_1850_1900.shape)
print("Pre-industrial dtype:", mean_1850_1900.dtype)

# Breakpoint for debugging
pdb.set_trace()

# SSP1-1.9 Scenario
ssp119_dset = xr.open_dataset(r"C:\Users\Mesha\geo_env course data\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp119_r1i1p1f1_gr1_201501-210012.nc")

# Calculate the mean temperature for 2071–2100
mean_2071_2100_ssp119 = np.mean(ssp119_dset['tas'].sel(time=slice('2071-01-01', '2100-12-31')), axis=0)

# Convert to Numpy array
mean_2071_2100_ssp119 = np.array(mean_2071_2100_ssp119)

# Check the shape and dtype of the result
print("SSP1-1.9 shape:", mean_2071_2100_ssp119.shape)
print("SSP1-1.9 dtype:", mean_2071_2100_ssp119.dtype)

# Convert temperature to Celsius
mean_2071_2100_ssp119 = mean_2071_2100_ssp119 - 273.15  # Future temperature in Celsius

# Calculate temperature difference
temp_difference = mean_2071_2100_ssp119 - mean_1850_1900

# Create the map for ssp119 vs 1850-1900
plt.figure(figsize=(10, 6))
plt.imshow(temp_difference, cmap='coolwarm', origin='lower')
plt.colorbar(label='Temperature Difference (°C)')
plt.title('Temperature Difference: SSP1-1.9 (2071–2100) vs Pre-industrial (1850–1900)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('temperature_difference_ssp119.png', dpi=300)
plt.show()

# Breakpoint for debugging
pdb.set_trace()

# SSP245 Scenario
ssp245_dset = xr.open_dataset(r"C:\Users\Mesha\geo_env course data\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp245_r1i1p1f1_gr1_201501-210012.nc")

# Calculate the mean temperature for 2071–2100
mean_2071_2100_ssp245 = np.mean(ssp245_dset['tas'].sel(time=slice('2071-01-01', '2100-12-31')), axis=0)

# Convert to Numpy array
mean_2071_2100_ssp245 = np.array(mean_2071_2100_ssp245)

# Check the shape and dtype of the result
print("SSP245 shape:", mean_2071_2100_ssp245.shape)
print("SSP245 dtype:", mean_2071_2100_ssp245.dtype)

# Convert temperatureto Celsius
mean_2071_2100_ssp245 = mean_2071_2100_ssp245 - 273.15 

# Calculate temperature difference
temp_difference_ssp245 = mean_2071_2100_ssp245 - mean_1850_1900

# Create the map for ssp245 vs 1850-1900
plt.figure(figsize=(10, 6))
plt.imshow(temp_difference_ssp245, cmap='coolwarm', origin='lower')
plt.colorbar(label='Temperature Difference (°C)')
plt.title('Temperature Difference: SSP2-4.5 (2071–2100) vs Pre-industrial (1850–1900)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('temperature_difference_ssp245.png', dpi=300)
plt.show()

# Breakpoint for debugging
pdb.set_trace()

#SSP585 Scenario
ssp585_dset = xr.open_dataset(r"C:\Users\Mesha\geo_env course data\Climate_Model_Data\tas_Amon_GFDL-ESM4_ssp585_r1i1p1f1_gr1_201501-210012.nc")


#Calculate the mean temp for the ssp585
mean_2071_2100_ssp585 = np.mean(ssp585_dset['tas'].sel(time=slice('2071-01-01', '2100-12-31')), axis=0)

# Convert to numpy array
mean_2071_2100_ssp585 = np.array(mean_2071_2100_ssp585)

# Check shape and dtype
print("SSP585 shape:", mean_2071_2100_ssp585.shape)
print("SSP585 dtype:", mean_2071_2100_ssp585.dtype)

# Convert temp from Kelvin to Celsius
mean_2071_2100_ssp585 = mean_2071_2100_ssp585 - 273.15

# Calculate the temp difference
temp_difference_ssp585 = mean_2071_2100_ssp585 - mean_1850_1900

# Create the map for ssp585 vs 1850-1900
plt.figure(figsize=(10, 6))
plt.imshow(temp_difference_ssp585, cmap='coolwarm', origin='lower')
plt.colorbar(label='Temperature Difference (°C)')
plt.title('Temperature Difference: SSP5-8.5 (2071–2100) vs Pre-industrial (1850–1900)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('temperature_difference_ssp585.png', dpi=300)
plt.show()

