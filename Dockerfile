# syntax=docker/dockerfile:1
#FROM --platform=$BUILDPLATFORM python:3.10-slim-bullseye
FROM python:3-slim

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 444 app.py
RUN chmod 444 requirements.txt

RUN apt-get update
RUN apt-get install -y npm
RUN npm install tailwindcss autoprefixer tailwindcss-fluid-type daisyui @tailwindcss/typography
RUN npx tailwindcss init -p
RUN npx tailwindcss -i ./static/src/main.css -o ./static/dist/main.css

ENV PORT 8080
# Run the web service on container startup.
CMD [ "waitress-serve", "--port $PORT", "app:app" ]