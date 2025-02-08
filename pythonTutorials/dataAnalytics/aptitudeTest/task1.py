import pandas as pd
from data_loader import load_data

# Write your code here
# def neighbourhood_with_highest_median_price_diff(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> str:
#     df_listings["price"] = df_listings["price"].astype("int")
#     median = df_listings.groupby('neighbourhood_cleansed')["price"].median()
#     return median 
 

''' 
MANDATORY - Explain your solution in plain english here
First, the data
Per the data available on the listings, the second row of the 
dataframe contains the non-superhost entry, so I decided to slice it out and
perform the analysis on only that row.


COMMENTS END
'''

# if __name__ == '__main__':
#     print('Neighborhood with highest price difference: ', neighbourhood_with_highest_median_price_diff(*load_data()))
df_listings, df_reviews = (load_data())

print(df_listings.head())