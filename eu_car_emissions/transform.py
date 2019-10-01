# import dask.dataframe as dd
import numpy as np
import pandas as pd
from pandas.util import hash_pandas_object
import schema_pandas as schema

def load_data(**kwargs):
    return pd.read_csv('CO2_passenger_cars_v16.csv', dtype=schema.schema, sep='\t',
        encoding='utf_16_le', **kwargs)

def load_sample():
    return load_data(nrows=100000)

# add a 'digest' column that calculates a hash per row from the values, skipping
# 'ID' and 'r'.
def add_digest(df):
    df['digest'] = hash_pandas_object(df.iloc[:, 1:-1], index=False)
    return df

def count_similar(group):
    out = group.iloc[0].copy()
    out['count'] = group['r'].sum()
    return out

def transform(df):
    return df.pipe(add_digest) \
             .groupby('digest') \
             .apply(count_similar) \
             .drop(['digest', 'ID', 'r'], axis=1)


if __name__ == "__main__":
    rows = 10000
    print(f'Loading {rows} rows')
    df = load_data(nrows=rows)
    print("Grouping similar entries...")
    df = transform(df)
    print("Saving...")
    df.to_csv('out.csv')
    print("Done.")
