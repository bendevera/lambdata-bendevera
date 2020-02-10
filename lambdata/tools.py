import pandas as pd 
import os

def test():
    print("Hello from lambdata-bendevera")

def df_null_report(df):
    print("-"*8+ " DF NULL REPORT " + "-"*8)
    for column in df.columns:
        print(f"{column} null count: ", df[column].isnull().sum())

if __name__ == "__main__":
    test()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    TEST_CSV = os.path.join(dir_path, "test_data/books.csv")
    df = pd.read_csv(TEST_CSV)
    df_null_report(df)