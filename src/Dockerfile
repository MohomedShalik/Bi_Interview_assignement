FROM python:3.11.6-slim-bookworm


ENV PYTHONUNBUFFERED=1


WORKDIR /src

RUN pip install django django-cors-headers pandas python-dotenv

COPY . .

WORKDIR /src


WORKDIR /src/data_viz_backend


EXPOSE 8000