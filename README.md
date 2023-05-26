# crypto-price-action-alerts
Django application service to send crypto price action trigger alerts to users

## Steps to run the code

1. create virtual env

`virtualenv venv`

2. activate the virtual env

`source venv/bin/activate`

3. install dependencies:

`pip install -r requirements.txt`


## Steps to run docker container

1. build docker image

`docker build -t crypto-price-action-alerts:latest .`

2. run the docker container

`docker run crypto-price-action-alerts:latest`
