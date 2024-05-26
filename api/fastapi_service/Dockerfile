FROM python:3.9-slim

WORKDIR /fastapi_service

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /fastapi_service
RUN chmod 755 ./wait-for-it.sh

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
EXPOSE 8000
