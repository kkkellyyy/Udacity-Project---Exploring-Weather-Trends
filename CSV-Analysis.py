# -*- coding: utf-8 -*-
"""
Spyder Editor

Creator: Simon Thornewill von Essen
"""

# Importing files
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Automatically get working directory
workingDirectory = os.getcwd()
csvDirPath = str(workingDirectory + "/CSV-data")

# Import datasets
berlinAvgTempDF = pd.read_csv(str(csvDirPath + "/BerlinYearlyAvgTemp.csv")) 
globalAvgTempDF = pd.read_csv(str(csvDirPath + "/GlobalYearlyAvgTemp.csv"))

"""
Upon investigating the datasets I found that berlinAvgTempDF has missing
values for a couple of years.

It should be noted that the shapes for each dataframe is also different this
because the global temperature starts 7 years after the temperature was init-
ially measured in Berlin. Additionally, there are an additional 2 years 
recorded for the global data.

In order not to impute more information than I need to, I will drop the first
7 rows of the Berlin temperature which will give the data the same shape while
also eliminating the NaN values in the Berlin data. 

Two rocks with one stone.(Which is unfornunate because I wanted to use some 
fancy code)
"""

# Drop rows before 1950 and reset index
berlinAvgTempDF = berlinAvgTempDF.iloc[7:, :]
berlinAvgTempDF = berlinAvgTempDF.reset_index(level = 0)
berlinAvgTempDF = berlinAvgTempDF.drop('index', 1)

# Drop rows after 2013
globalAvgTempDF = globalAvgTempDF.iloc[:-2, :]

"""
Next, we'll want to calculare the moving averages before doing the final plot

This next code gets pretty sticky, for feedback I would like to know how I
could make this code simpler and easier to read.

note that the variable "moving" can be changed to give moving averages (M.A.) 
over different spans such as a 7 year M.A. or 2 year M.A.
"""

# Calculation
moving = 7
averageBerlin = []
averageGlobal = []
for i in range(len(berlinAvgTempDF)):
    averageBerlin.append(np.average(berlinAvgTempDF.iloc[(i-moving):i, 1]))
    averageGlobal.append(np.average(globalAvgTempDF.iloc[(i-moving):i, 1]))
berlinAvgTempMovingAverageDF = berlinAvgTempDF
globalAvgTempMovingAverageDF = globalAvgTempDF
for i in range(len(berlinAvgTempDF)):   
    berlinAvgTempMovingAverageDF.iloc[i, 1] = averageBerlin[i]
    globalAvgTempMovingAverageDF.iloc[i, 1] = averageGlobal[i]

# Dropping null values
berlinAvgTempMovingAverageDF = berlinAvgTempMovingAverageDF.iloc[7:, :]
berlinAvgTempMovingAverageDF = berlinAvgTempMovingAverageDF.reset_index(level = 0)
berlinAvgTempMovingAverageDF = berlinAvgTempMovingAverageDF.drop('index', 1)
    
globalAvgTempMovingAverageDF = globalAvgTempMovingAverageDF.iloc[7:, :]
globalAvgTempMovingAverageDF = globalAvgTempMovingAverageDF.reset_index(level = 0)
globalAvgTempMovingAverageDF = globalAvgTempMovingAverageDF.drop('index', 1)

"""
For some reason this code ends up turning every value in the dataframe into
a null value and I don't know why:

berlinAvgTempMovingAverageDF = berlinAvgTempDF
globalAvgTempMovingAverageDF = globalAvgTempDF
for i in range(len(berlinAvgTempDF)):
    berlinAvgTempMovingAverageDF.iloc[i, 1] = np.average(berlinAvgTempDF.iloc[(i-moving):i, 1])
    globalAvgTempMovingAverageDF.iloc[i, 1] = np.average(globalAvgTempDF.iloc[(i-moving):i, 1])
    
My suspicion is that the copied dataframes are lined in some way such that if
I change one, the other changes as well but that shouldn't be the case

I am aware that this will throw a warning and a bunch of null values which I
plan to deal with in the next code section
"""
    
# Draw graph in matplotlib
print('Creating Plot...')
plt.plot(berlinAvgTempMovingAverageDF['year'], berlinAvgTempMovingAverageDF['avg_temp'], label='Berlin')
plt.plot(globalAvgTempMovingAverageDF['year'], globalAvgTempMovingAverageDF['avg_temp'], label='Global')
plt.legend()
plt.xlabel("Year (C.E.)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Berlin versus Global values")
plt.show()

print('Complete! Exiting now.')