FROM python:3.8.8-slim-buster

WORKDIR /app

ADD ./src/requirements.txt .

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY ./src .

EXPOSE 8002

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
