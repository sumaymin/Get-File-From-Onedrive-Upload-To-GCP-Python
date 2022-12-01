from google.cloud import storage
import os

# Access to GCP
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = {your_api_gcp_json}
storage_client = storage.Client()
bucket_name = {your_bucket_name}
file_bucket = storage_client.get_bucket(bucket_or_name = bucket_name)

# Upload files
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

file_path = {your_file_path}

for i in range(len(file)):
    upload_to_bucket(file[i], os.path.join(file_path,file[i]), bucket_name)