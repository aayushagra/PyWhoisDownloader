# PyWhoisDownloader
Celery worker to download and save WHOIS data of a domain to Google Cloud Storage

To use this script, first you need to edit these two variables inside the tasks.py file:

broker      = ""    
#Celery Compatible message broker Example: redis://127.0.0.1

bucket_name = ""
#Name of the Google Cloud Bucket

Use the following command to run the Celery worker:

celery -A tasks.py worker --concurrency=1

Note that the concurrency=1 part is important. Without it, a single worker will make more than one request per second and get blocked.

To run the script on multiple workers, build and run the script through the dockerfile provided

FAQ

Why doesn't a single worker do multiple requests?
  More than 1 requests per second gets the worker's IP blocked. This script was built around the idea of using multiple cloud servers to do the job since it's cheap to run dozens of shared CPU cloud servers for a few hours
