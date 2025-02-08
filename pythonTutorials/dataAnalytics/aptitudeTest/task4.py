import pandas as pd
from data_loader import load_data

# Write your code here
def price_premium_for_entire_homes(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    return 0.00


''' 
MANDATORY - Explain your solution in plain english here



COMMENTS END
'''

if __name__ == '__main__':
    print('Price premium for entire homes is: ', price_premium_for_entire_homes(*load_data()))