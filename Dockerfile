FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY uv.lock pyproject.toml /app/

RUN uv sync --all-extras

COPY . /app/

ENV PYTHONWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

CMD uv run pytest
