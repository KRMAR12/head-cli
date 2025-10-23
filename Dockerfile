FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir .

ENTRYPOINT ["python", "-m", "head_cli"]
