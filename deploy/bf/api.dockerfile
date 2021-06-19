FROM python:3.8.8-slim-buster

WORKDIR /app

RUN python -m pip install -U pip poetry &&\
    poetry config virtualenvs.create false

ADD pyproject.toml poetry.lock ./

RUN poetry install

COPY ./src .

EXPOSE 8002

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
