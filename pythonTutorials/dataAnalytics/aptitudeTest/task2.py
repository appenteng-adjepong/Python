import pandas as pd
from data_loader import load_data

# Write your code here
def review_score_with_highest_correlation_to_price(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> str:
    return ''

''' 
MANDATORY - Explain your solution in plain english here



COMMENTS END
'''

if __name__ == '__main__':
    print('Review score with max correlation to price is: ', review_score_with_highest_correlation_to_price(*load_data()))