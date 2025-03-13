# Dockerfile
FROM python:3.11.9-slim
WORKDIR /app
COPY . ./
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"
# Dockerfile
EXPOSE 10000
