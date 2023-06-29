FROM python:3.11.4-slim

WORKDIR /app

COPY . /app/

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --only main --no-root

EXPOSE 8080

# CMD ["python", "main.py"]