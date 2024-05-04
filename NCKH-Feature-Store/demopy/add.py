from google.cloud import bigquery
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/Hovoh/Downloads/pythonkey.json"

# Construct a BigQuery client object.
client = bigquery.Client()
table_id = "feature-store-345214.raw_data.data_table"

rows_to_insert = [  
    {"is_prossesing": False},
]

errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))