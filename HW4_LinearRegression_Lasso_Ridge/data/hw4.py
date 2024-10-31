import pandas as pd
# these two files are large, and it may take a while to read...
counts = pd.read_csv('FremontBridge.csv', index_col='Date', parse_dates=True)
weather = pd.read_csv('BicycleWeather.csv', index_col='DATE', parse_dates=True)

print(len(counts))
print(len(weather))
print(counts[:5])
print(weather[:5])