python -m pip install -r /app/requirements.txt
cd /app/src/pywhoami
python -m hypercorn --bind=0.0.0.0:8080 --reload --access-logfile - asgi:app
