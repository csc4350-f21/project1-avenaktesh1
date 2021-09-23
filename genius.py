import requests
import json
import os
import random
from spotify import get_spotify_data
from dotenv import find_dotenv, load_dotenv

# Environment variables
load_dotenv(find_dotenv())

# Client Credentials Flow Authorization URL
AUTH_URL = "https://api.genius.com/oauth/token"

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
