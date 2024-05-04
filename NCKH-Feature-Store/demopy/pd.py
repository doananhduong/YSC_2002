import pandas as pd
from pandas.io import gbq
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/Hovoh/Downloads/pythonkey.json"
from google.cloud import bigquery

df = """ SELECT * FROM `feature-store-345214.raw_data.raw_data_table`"""
df = gbq.read_gbq(df, project_id = "feature-store-345214")

df1 = df[df['is_processed'] == False]

if df[df['is_processed'] == False].empty:
  print('Khong co data can xu ly')
else:
  df[df['is_processed'] == False].dropna(axis = 0)
  df[df['is_processed'] == False] = True

print(df[df['is_processed'] == False].count())