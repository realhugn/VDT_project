FROM python:3.9-slim

WORKDIR /fastapi_service

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install fastapi uvicorn

COPY . /fastapi_service
RUN chmod 755 ./wait-for-it.sh

EXPOSE 8000