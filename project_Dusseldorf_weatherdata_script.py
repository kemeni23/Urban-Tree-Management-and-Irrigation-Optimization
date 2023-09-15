

import pandas as pd # library for data management

import matplotlib
import matplotlib.pyplot as plt #Library for plotting


### Importing the data
city = pd.read_excel(r"D:\Project_weather\Wetterstation_city.xlsx", header = 0, na_values=['noData', '99999'], decimal=",")
city.columns = ['timestamp', 'temperature', 'day length', 'precipitation']
print(city.head())
city.info()
## Converting the timestamp from object to datetime format
city['timestamp'] = pd.to_datetime(city['timestamp'], utc=True, format= '%d.%m.%Y')
## Setting the timestamp column as index
city = city.set_index('timestamp')
print(city.index)
## Slicing the dataframe from April to September
city = city['2020-04-01':'2020-09-30']
y = city['precipitation']

city_weekly= city.resample('W').mean()


## Creating a loop to distinguish the colour in case of daily data
#col = []
#for val in y:
    #if val > 1:
        #col.append('blue')
    #else:
        #col.append('red')

## Plotting
fig, ax = plt.subplots(figsize=(10, 7))
# to plot scatter plot use ax.scatter() command 
#ax.bar(city_weekly.index, y, color = col)
ax.bar(city_weekly.index,city_weekly['precipitation'])
# Set title and labels for axes
ax.set_xlabel("Date", fontsize = 30)
ax.set_ylabel("Precipitation (mm)", fontsize = 30)
#ax.set_xlim(0, 50)
#ax.set_ylim(8.6, 13.5)
#ax.set_title("GR1", fontsize = 35)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.tight_layout()
#plt.savefig("D:\Py_analysis\Figure_for_2023_analysis\Kdose_SM.png")
plt.show()
