# -*- coding: utf-8 -*-
"""
Spyder Editor

Creator: Simon Thornewill von Essen
"""

# Importing files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import datasets
df = pd.read_csv("YearlyAvgTemp.csv") 

"""
Next, we'll want to calculate the moving averages before doing the final plot

In my project submission I chose a moving average of 7 but this did not give a
smooth curve that was expected according to my feedback and I need to chose a
larger range. Given that the data spans around 200 years I'll want to
investigate 10 years and 100 years and maybe sharpen things from there
"""

# Calculation
df_movingAverage = df.rolling(window = 100, center=False, on = "year").mean().dropna()


# Draw graph in matplotlib
print('Creating Plot...')
plt.plot(df_movingAverage['year'], df_movingAverage['city_avg_temp'], label='Berlin')
plt.plot(df_movingAverage['year'], df_movingAverage['global_avg_temp'], label='Global')
plt.legend()
plt.xlabel("Year (C.E.)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Berlin versus Global values")
plt.show()