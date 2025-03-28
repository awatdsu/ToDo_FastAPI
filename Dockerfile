FROM python:3.11.9-slim

WORKDIR /app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "app"]
