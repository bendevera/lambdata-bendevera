import pandas as pd 
from sklearn.model_selection import train_test_split
import os

def test():
    print("Hello from lambdata-bendevera")

def df_null_report(df):
    print("-"*8+ " DF NULL REPORT " + "-"*8)
    for column in df.columns:
        print(f"{column} null count: ", df[column].isnull().sum())

def train_test_val_split(df):
    '''
    This function performs a train, val, test split on a dataframe.
    '''
    train, test = train_test_split(df, test_size=.2)
    train, val = train_test_split(train, test_size=.2)
    print("TRAIN/TEST/VAL Breakdown:")
    print(f"TRAIN : {train.shape}")
    print(f"TEST : {test.shape}")
    print(f"VAL : {val.shape}")
    return train, test, val

if __name__ == "__main__":
    test()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    TEST_CSV = os.path.join(dir_path, "test_data/books.csv")
    df = pd.read_csv(TEST_CSV)
    df_null_report(df)
    train, test, val = train_test_val_split(df)