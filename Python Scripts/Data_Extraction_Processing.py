import requests
import pandas as pd
from datetime import datetime
import io

# API_KEY = '8256AHZLLZR2AACRCHTY6HVU6'
# LOCATION = 'Kolkata,India'
# BASE_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'

# # Date chunks (max 1 year per request)
# date_ranges = [
#     ('2020-01-01', '2020-12-31'),
#     ('2021-01-01', '2021-12-31'),
#     ('2022-01-01', '2022-12-31'),
#     ('2023-01-01', '2023-12-31'),
#     ('2024-01-01', '2024-12-31'),
#     ('2025-01-01', '2025-07-21'),  # Up to today
# ]

# all_dfs = []

# for start, end in date_ranges:
#     print(f"Fetching data from {start} to {end}")
#     url = f"{BASE_URL}/{LOCATION}/{start}/{end}?unitGroup=metric&include=days&key={API_KEY}&contentType=csv"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         temp_df = pd.read_csv(io.StringIO(response.text))
#         all_dfs.append(temp_df)
#     else:
#         print(f"Error fetching data for {start} to {end}: {response.status_code}")

# # Combine all parts into one DataFrame
# weather_df = pd.concat(all_dfs, ignore_index=True)
# # weather_df.to_csv('kolkata_weather_2020_2025.csv', index=False)
# # print("✅ Data saved to kolkata_weather_2020_2025.csv")
# # # Display the first few rows of the DataFrame
# # print(weather_df.head())

kol_weather_df = pd.read_excel('Kolkata Weather 2020-2025.xlsx')
# print(kol_weather_df.head())
print(kol_weather_df.isnull().sum())
kol_weather_df['datetime'] = pd.to_datetime(kol_weather_df['datetime'])
print(kol_weather_df.dtypes)
print(kol_weather_df.columns)
# save the DataFrame to a CSV file
kol_weather_df.to_csv('kolkata_weather_2020_2025_final.csv', index=False)
print("✅ Data saved to kolkata_weather_2020_2025_final.csv")