import pandas as pd

# File paths
file_path_tesla = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\TESLA Search Trend vs Price.csv'
file_path_btc_search = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\Bitcoin Search Trend.csv'
file_path_btc_price = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\Daily Bitcoin Price.csv'
file_path_unemployment_2004_2019 = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\UE Benefits Search vs UE Rate 2004-19.csv'
file_path_unemployment_2004_2020 = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0079__Day75_GoogleData_Resampling_and_Visualizing_Time_Series_240819\NewProject\r00-r09 START\r00_env_START\UE Benefits Search vs UE Rate 2004-20.csv'

# Load the data into DataFrames
df_tesla = pd.read_csv(file_path_tesla)
df_btc_search = pd.read_csv(file_path_btc_search)
df_btc_price = pd.read_csv(file_path_btc_price)
df_unemployment_2004_2019 = pd.read_csv(file_path_unemployment_2004_2019)
df_unemployment_2004_2020 = pd.read_csv(file_path_unemployment_2004_2020)

# Get the max and min values in the WEB_SEARCH columns
max_tesla_search = df_tesla['TSLA_WEB_SEARCH'].max()
min_tesla_search = df_tesla['TSLA_WEB_SEARCH'].min()

max_btc_search = df_btc_search['BTC_NEWS_SEARCH'].max()
min_btc_search = df_btc_search['BTC_NEWS_SEARCH'].min()

max_btc_price = df_btc_price['CLOSE'].max()
min_btc_price = df_btc_price['CLOSE'].min()

max_unemployment_2004_2019 = df_unemployment_2004_2019['UE_BENEFITS_WEB_SEARCH'].max()
min_unemployment_2004_2019 = df_unemployment_2004_2019['UE_BENEFITS_WEB_SEARCH'].min()

max_unemployment_2004_2020 = df_unemployment_2004_2020['UE_BENEFITS_WEB_SEARCH'].max()
min_unemployment_2004_2020 = df_unemployment_2004_2020['UE_BENEFITS_WEB_SEARCH'].min()

# Print the results
print(f"Max Tesla Web Search: {max_tesla_search}, Min Tesla Web Search: {min_tesla_search}")
print(f"Max Bitcoin Web Search: {max_btc_search}, Min Bitcoin Web Search: {min_btc_search}")
print(f"Max Bitcoin Price: {max_btc_price}, Min Bitcoin Price: {min_btc_price}")
print(f"Max Unemployment Web Search 2004-2019: {max_unemployment_2004_2019}, Min Unemployment Web Search 2004-2019: {min_unemployment_2004_2019}")
print(f"Max Unemployment Web Search 2004-2020: {max_unemployment_2004_2020}, Min Unemployment Web Search 2004-2020: {min_unemployment_2004_2020}")
