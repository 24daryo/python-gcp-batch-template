FROM python:3.11-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME ./app
WORKDIR $APP_HOME
COPY ./src ./

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
CMD python main.py