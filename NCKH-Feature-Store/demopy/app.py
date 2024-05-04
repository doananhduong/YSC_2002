
from pickle import TRUE
import pandas as pd
from pandas.io import gbq
import pandas_gbq
import flask
from flask import request, jsonify, json
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:/NCKH-Feature-Store-demo-/key.json"
from google.cloud import bigquery
bigquery_client = bigquery.Client()
query_job = bigquery_client.query(
  """
  SELECT
    *
  FROM 
    `modular-seeker-345718.feature_store.raw_data`
  WHERE is_processed = False
  """
)
df = query_job.to_dataframe()
app = flask.Flask(__name__,template_folder='templates')
@app.route("/")
def main():
  return flask.render_template("query_result.html", results=query_job.result())

@app.route("/processing/", methods=["POST"])
def processing_data():
  if df[df['is_processed'] == False].empty:
    return 'No data to process'
  else:
    
    df['is_processed'].replace({False: True}, inplace=True)
    pandas_gbq.to_gbq(df, 'feature_store.raw_data', project_id="modular-seeker-345718", if_exists = 'replace')
    pandas_gbq.to_gbq(df, 'feature_store.feature_store', project_id="modular-seeker-345718", if_exists = 'append')
  return 'Data Processed !!'


ALLOWED_EXTENSIONS = {'csv'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER = '/data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/insert/", methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
      file = request.files['file']
      add_column = pd.read_csv(file.filename)
      add_column = add_column.assign(is_processed=False)
      add_column.to_csv(file.filename, index=False, header=True)
      if file:
        client = bigquery.Client(project="modular-seeker-345718")
        table_ref = client.dataset("feature_store").table("raw_data")
        job_config = bigquery.LoadJobConfig()
        job_config.source_format = bigquery.SourceFormat.CSV
        job_config.skip_leading_rows = 1 # ignore the header
        job_config.autodetect = True
        with open(file.filename, "rb") as source_file:
            job = client.load_table_from_file(
              source_file, table_ref, job_config=job_config
            ) 
          # job is async operation so we have to wait for it to finish
            job.result()
  return 'upload sucess!'
      
  
if __name__ == "__main__":
    app.run(port=8080, debug=True)