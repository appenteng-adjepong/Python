import pandas as pd
from data_loader import load_data

# Write your code here
def prof_nonprof_host_price_diff(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    return 0.00

''' 
MANDATORY - Explain your solution in plain english here



COMMENTS END
'''

if __name__ == '__main__':
    print('Professional Host Analysis: ', prof_nonprof_host_price_diff(*load_data()))