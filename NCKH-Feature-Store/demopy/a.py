from google.cloud import bigquery
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/Hovoh/Downloads/pythonkey.json"

# Construct a BigQuery client object.
client = bigquery.Client()

table_id = "feature-store-345214.raw_data.data_raw"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)

with open('D:/datatest/Sample - Superstore/Sample - Superstore/split_data/raw_data_90.csv', "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)