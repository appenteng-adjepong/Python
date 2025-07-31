import pandas as pd

def _load_listings_data():
    """
    Returns the Airbnb listings dataset as a pd.DataFrame.
    """
    return pd.read_csv(r"C:\Users\appenteng.adjepong\Desktop\Datasets\new_orleans_airbnb_listings.csv", low_memory=False)

def _load_reviews_data():
    """
    Returns the Airbnb reviews dataset as a pd.DataFrame.
    """
    return pd.read_csv(r"C:\Users\appenteng.adjepong\Desktop\Datasets\new_orleans_airbnb_reviews.csv", low_memory=False)

def load_data():
    """
    Returns the Airbnb listings and reviews datasets as a tuple of pd.DataFrame.
    """
    return _load_listings_data(), _load_reviews_data()