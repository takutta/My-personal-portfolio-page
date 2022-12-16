# syntax=docker/dockerfile:1
#FROM --platform=$BUILDPLATFORM python:3.10-slim-bullseye
FROM python:3-slim
#WORKDIR /My-personal-portfolio-page

#COPY requirements.txt requirements.txt

#RUN --mount=type=cache,target=/root/.cache/pip \
#    pip3 install -r requirements.txt

#COPY . .

#CMD ["gunicorn"  , "-b", "0.0.0.0:8888", "app:app"]

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 444 app.py
RUN chmod 444 requirements.txt

RUN apt-get update
RUN apt-get install npm
RUN npm install tailwindcss autoprefixer tailwindcss-fluid-type daisyui @tailwindcss/typography
RUN npx tailwindcss init -p
RUN npx tailwindcss -i ./static/src/main.css -o ./static/dist/main.css

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080

# Run the web service on container startup.

CMD [ "python", "app.py" ]
