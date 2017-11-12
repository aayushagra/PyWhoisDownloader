# PyWhoisDownloader
Celery worker to download and save WHOIS data of a domain to Google Cloud Storage

Use the following command to run the Celery worker:

celery -A tasks.py worker --concurrency=1

Note that the concurrency=1 part is important. Without it, a single worker will make more than one request per second and get blocked.

To run the script on multiple workers, build and run the script through the dockerfile provided
