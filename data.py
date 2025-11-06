import requests
from env import * # uncomment if you don't create an env.py file

# CONSTANTS

## WEB SERVICE DEPLOYMENT
#HOSTNAME = "insert.hostname"
#PORT = 8888
#SSL_KEY_PATH = "insert/path"
#SSL_CERT_PATH = "insert/path"

## FRONTLINE USER
#USERNAME = "username"
#PASSWORD = "password"

## FRONTLINE REQUESTS
FRONTLINE_DOMAIN = "https://frontlineworker.com/"
CLIENT_DOMAIN = "adaptit"
FULL_DOMAIN = FRONTLINE_DOMAIN + CLIENT_DOMAIN

AUTH_URL = FULL_DOMAIN + "/login"
AUTH_HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

AUTH_BODY = {
    "agreedToTos": True,
    "domain": "ubimax",
    "password": PASSWORD,
    "username": USERNAME
}

GET_IMG_URL = FULL_DOMAIN + "/assets/download_asset_by_uri"

GET_IMG_PARAMS = {
    "uri": "",
    "size": "SMALL"
}

GET_IMG_HEADERS = {
    'accept': 'application/octet-stream',
    'Authorization': "",
}

# FUNCTIONS

## Authenticate user and return user token
def authenticate():
    r = requests.post(url=AUTH_URL, headers=AUTH_HEADERS, json=AUTH_BODY)
    if r.status_code != 200:
        return r.text
    
    token = r.json()['token']
    return token

## Send the GET request with the URI to download the respective image
def downloadImage(uri, token):
    GET_IMG_PARAMS['uri'] = uri
    GET_IMG_HEADERS['Authorization'] = "Bearer " + token

    r = requests.get(url=GET_IMG_URL, params= GET_IMG_PARAMS, headers=GET_IMG_HEADERS)
    # The payload is stored in r.content
    return r.status_code
    

