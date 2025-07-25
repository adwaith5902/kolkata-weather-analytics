import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_excel('kolkata_weather_2020_2025_final.xlsx')
   
# print(df.head())

df['ds'] = pd.to_datetime(df['Date'])
# Rename avg temp column to 'y'
df['y'] = df['Avg Temp']
df = df[['ds', 'y']]

# print(df.head())

model = Prophet()      
model.fit(df)          # Training the model
print("✅ Model trained successfully")

future = model.make_future_dataframe(periods=163)
forecast = model.predict(future)

forecast_avg = forecast[forecast['ds'] > '2025-07-21']
# Print the first few rows
print(forecast_avg[['ds', 'yhat']].head())

forecast_avg = forecast_avg[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
forecast_avg.columns = ['ds', 'avg_temp', 'avg_temp_lower', 'avg_temp_upper']

# model.plot(forecast)
# plt.title("Forecast of Avg Temp (Jul 22 – Dec 2025)")
# plt.xlabel("Date")
# plt.ylabel("Avg Temp")
# plt.show()
df = pd.read_excel('kolkata_weather_2020_2025_final.xlsx')

# print(df.head())

# Min Temp
df['ds'] = pd.to_datetime(df['Date'])
df['y'] = df['Min Temp']
df_min = df[['ds', 'y']]
model_min = Prophet()
model_min.fit(df_min)
print("✅ Min Temp model trained successfully")
future_min = model_min.make_future_dataframe(periods=163)
forecast_min = model_min.predict(future_min)
forecast_min = forecast_min[forecast_min['ds'] > '2025-07-21']
forecast_min = forecast_min[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
forecast_min.columns = ['ds', 'min_temp', 'min_temp_lower', 'min_temp_upper']

# Max Temp
df['y'] = df['Max Temp']
df_max = df[['ds', 'y']]
model_max = Prophet()
model_max.fit(df_max)
print("✅ Max Temp model trained successfully")
future_max = model_max.make_future_dataframe(periods=163)
forecast_max = model_max.predict(future_max)
forecast_max = forecast_max[forecast_max['ds'] > '2025-07-21']
forecast_max = forecast_max[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
forecast_max.columns = ['ds', 'max_temp', 'max_temp_lower', 'max_temp_upper']

# Precipitation
df['y'] = df['Precipitation']
df_precip = df[['ds', 'y']]
model_precip = Prophet()
model_precip.fit(df_precip)
print("✅ Precipitation model trained successfully")
future_precip = model_precip.make_future_dataframe(periods=163)
forecast_precip = model_precip.predict(future_precip)
forecast_precip = forecast_precip[forecast_precip['ds'] > '2025-07-21']
forecast_precip = forecast_precip[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
forecast_precip.columns = ['ds', 'precipitation', 'precipitation_lower', 'precipitation_upper']

# Feels Like
df['y'] = df['Feels_Like']
df_feels = df[['ds', 'y']]
model_feels = Prophet()
model_feels.fit(df_feels)
print("✅ Feels Like model trained successfully")
future_feels = model_feels.make_future_dataframe(periods=163)
forecast_feels = model_feels.predict(future_feels)
forecast_feels = forecast_feels[forecast_feels['ds'] > '2025-07-21']
forecast_feels = forecast_feels[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
forecast_feels.columns = ['ds', 'feels_like', 'feels_like_lower', 'feels_like_upper']

# Max Feels Like
df['y'] = df['Max_Feels_Like']
df_max_feel = df[['ds', 'y']]
model_max_feel = Prophet()
model_max_feel.fit(df_max_feel)
print("✅ Max Feels Like model trained successfully")
future_max_feel = model_max_feel.make_future_dataframe(periods=163)
forecast_max_feel = model_max_feel.predict(future_max_feel)
forecast_max_feel = forecast_max_feel[forecast_max_feel['ds'] > '2025-07-21']
forecast_max_feel = forecast_max_feel[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
forecast_max_feel.columns = ['ds', 'max_feels_like', 'max_feels_like_lower', 'max_feels_like_upper']

# Min Feels Like
df['y'] = df['Min_Feels_Like']
df_min_feel = df[['ds', 'y']]
model_min_feel = Prophet()
model_min_feel.fit(df_min_feel)
print("✅ Min Feels Like model trained successfully")
future_min_feel = model_min_feel.make_future_dataframe(periods=163)
forecast_min_feel = model_min_feel.predict(future_min_feel)
forecast_min_feel = forecast_min_feel[forecast_min_feel['ds'] > '2025-07-21']
forecast_min_feel = forecast_min_feel[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
forecast_min_feel.columns = ['ds', 'min_feels_like', 'min_feels_like_lower', 'min_feels_like_upper']

# Humidity
df['y'] = df['Humidity']
df_humidity = df[['ds', 'y']]
model_humidity = Prophet()
model_humidity.fit(df_humidity)
print("✅ Humidity model trained successfully")
future_humidity = model_humidity.make_future_dataframe(periods=163)
forecast_humidity = model_humidity.predict(future_humidity)
forecast_humidity = forecast_humidity[forecast_humidity['ds'] > '2025-07-21']
forecast_humidity = forecast_humidity[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
forecast_humidity.columns = ['ds', 'humidity', 'humidity_lower', 'humidity_upper']

from functools import reduce
# Combine all forecasts into one DataFrame
forecast_combined = reduce(lambda left, right: pd.merge(left, right, on='ds', how='outer'),
                            [forecast_avg, forecast_min, forecast_max, forecast_precip,        
                             forecast_feels, forecast_max_feel, forecast_min_feel, forecast_humidity])
#Sort the DataFrame by date
forecast_combined.sort_values(by='ds', inplace=True)
# Save the combined forecast to a CSV file
forecast_combined.to_csv('kolkata_weather_forecast_2025.csv', index=False)


