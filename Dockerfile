# Use the official image as a parent image.
FROM python:3.6.7-slim

# Set the working directory.
WORKDIR /usr/python-docker-example

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./example/calc.py" ]