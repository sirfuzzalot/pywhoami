python -m pip install -r /app/requirements.txt
cd /app/src
hypercorn --bind=0.0.0.0:8080 --reload --access-logfile - server:app
