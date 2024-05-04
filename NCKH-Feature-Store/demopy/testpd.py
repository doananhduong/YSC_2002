import pandas as pd
from pandas.io import gbq
import pandas_gbq
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/Hovoh/Downloads/pythonkey.json"
from google.cloud import bigquery

bigquery_client = bigquery.Client()
query_job = bigquery_client.query(
        """
        SELECT
          *
        FROM 
          `feature-store-345214.raw_data.new_data`
        """
)

df = query_job.to_dataframe()
if df[df['is_processed'] == False].empty:
  print('0')
else:
  print('1')
  df['is_processed'] = True

print(df[df['is_processed'] == False])
pandas_gbq.to_gbq(df, 'raw_data.table_processed', project_id="feature-store-345214", if_exists = 'replace')