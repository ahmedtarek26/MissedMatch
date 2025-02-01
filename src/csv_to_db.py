import sqlite3
import pandas as pd

df = pd.read_csv('/workspaces/MissedMatch/data/processed/KaggleV2-May-2016-proccessed.csv')

df.columns = df.columns.str.strip()

connection = sqlite3.connect('data/processed/MissedMatch.db')

df.to_sql('KaggleV2',connection,if_exists='replace')

connection.close()

