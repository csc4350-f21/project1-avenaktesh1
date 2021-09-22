import requests
import json
import os
import random
from spotify import get_spotify_data
from dotenv import find_dotenv, load_dotenv

# Environment variables
load_dotenv(find_dotenv())

# Client ID and Client Secret from the Genius web dashboard portal from .env
CLIENT_ID = os.getenv('CLIENT_ID_genius')
CLIENT_SECRET = os.getenv('CLIENT_SECRET_genius')

# Client Credentials Flow Authorization URL
AUTH_URL = "https://api.genius.com/oauth/token"

# Post request to generate authorization token
auth_response = requests.post(AUTH_URL, {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET
})

# Jsonify authorization response
auth_response_data = auth_response.json()

# Acces the 'access_token' credentials from the JSON object
access_token = auth_response_data['access_token']

# Import the auth token into the Authorization key header
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = "api.genius.com/artists/16775/songs" + song_info[5]
