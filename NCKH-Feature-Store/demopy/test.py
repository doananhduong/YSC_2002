from google.cloud import bigquery
import os 
import pandas as pd
# path = 'C:/Users/Hovoh/Downloads/feature-store-345214-b8f1c6d0cf0b.json'
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path

# client = bigquery.Client()
# # table_id = 'feature-store-345214.raw_data.data_table'
# # query = """
# #     SELECT *
# #     FROM `feature-store-345214.raw_data.data_table`
# # """
# query = (
#   'SELECT * FROM `feature-store-345214.raw_data.data_table'
# )
insert_data = pd.read_excel('./data.xlsx')
a = pd.DataFrame(insert_data)
# query_job = client.query(query)
print(a)
