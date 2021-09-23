import requests
import json
import os
import random
from spotify import get_spotify_data
from dotenv import find_dotenv, load_dotenv

# Environment variables
load_dotenv(find_dotenv())

# Client ID and Client Secret from the Genius web dashboard portal from .env
CLIENT_ID_genius = os.getenv('CLIENT_ID_genius')
CLIENT_SECRET_genius = os.getenv('CLIENT_SECRET_genius')

# Client Credentials Flow Authorization URL
AUTH_URL = "https://api.genius.com/oauth/token"

# Post request to generate authorization token
auth_response = requests.post(AUTH_URL, {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID_genius,
    "client_secret": CLIENT_SECRET_genius
})

# Jsonify authorization response
auth_response_data = auth_response.json()

# Acces the 'access_token' credentials from the JSON object
access_token = auth_response_data['access_token']
access_token = os.getenv('CLIENT_ACCESS_TOKEN')

# Import the auth token into the Authorization key header
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = "http://api.genius.com/search?q=" + get_spotify_data()[1] + "?" 

response = requests.get(
    BASE_URL,
    headers=headers
)
def get_genius_data():
    genius_url = []
    genius_url.append(response.json()['response']['hits'][0]['result']['url'])
    return genius_url
