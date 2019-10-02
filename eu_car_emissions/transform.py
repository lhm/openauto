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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--rows', type=int, default=10000,
        help='number of rows to process (default: %(default)s)')
    parser.add_argument('-a', '--all', dest='rows',action='store_const',
        const=None, help='process full file')
    args = parser.parse_args()
    rows = args.rows

    print(('Loading {} rows ').format((rows if rows else 'all')))
    df = load_data(nrows=rows)
    print("Grouping similar entries...")
    df = transform(df)
    print("Saving...")
    df.to_csv('out.csv')
    print("Done.")
