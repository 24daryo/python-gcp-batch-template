from google.cloud import storage

import configs as C


storage_client = storage.Client()
bucket = storage_client.get_bucket(C.CLOUD_STORAGE_BUCKET)

def list_files(folder_name):
    blobs = bucket.list_blobs(prefix=folder_name)
    return [blob.name for blob in blobs]
