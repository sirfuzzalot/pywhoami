FROM python:3.8-alpine

RUN addgroup python && adduser --system python

COPY --chown=python:python ./src /app/src/

COPY --chown=python:python  requirements.txt /app/

RUN python -m pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/src

USER python

CMD [ "hypercorn", "--bind=0.0.0.0:8080", "--access-logfile", "-", "--log-level", "warning", "server:app" ]

EXPOSE 8080
