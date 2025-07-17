import pandas as pd
import os

def load_site_data(filename="toll_sites.csv"):
    path = os.path.join(os.path.dirname(__file__), "..", "data", filename)
    return pd.read_csv(path)

