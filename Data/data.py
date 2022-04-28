import pandas as pd


def get_data(path):
    return pd.read_csv(path,index_col=0, header=None)
