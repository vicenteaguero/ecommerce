FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --only main --no-root

COPY app ./app

EXPOSE 8501
CMD ["streamlit", "run", "app/app.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
