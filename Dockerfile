FROM python:3.11

WORKDIR /app

RUN apt-get update && \
    apt-get install -y tesseract-ocr

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

COPY . .

CMD ["uvicorn", "image_analyzer.main:app", "--host", "0.0.0.0", "--port", "8000"]