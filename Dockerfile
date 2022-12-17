FROM python:3.10-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 444 app.py
RUN chmod 444 requirements.txt

RUN apt-get update
RUN apt-get install -y npm
RUN npm install tailwindcss autoprefixer daisyui @tailwindcss/typography
RUN npx tailwindcss init -p
RUN npx tailwindcss -i ./static/src/main.css -o ./static/dist/main.css

ENV PORT 8080
ENV FLASK_ENV=production
# Run the web service on container startup.
CMD [ "waitress-serve", "--port", "8080", "app:app" ]