broker      = ""    #Celery Compatible message broker. Example: redis://127.0.0.1
bucket_name = ""    #Name of the Google Cloud Bucket

from celery import Celery
import time
import whois
import json

from google.cloud import storage
from google.cloud.storage import Blob

client = storage.Client.from_service_account_json("apikey.json")

app = Celery('tasks', broker='redis://146.148.92.141:443')

@app.task(acks_late=True)
def add(x):
    time.sleep(1)
    bucket = client.get_bucket('testdownload12')
    blob = Blob("%s" % x, bucket)
    x = x.encode("UTF8")
    whoisdata = whois.whois(x)

    whoisdata = json.dumps(whoisdata, indent=4, sort_keys=True, default=str)

    blob.upload_from_string(whoisdata)
    return x
