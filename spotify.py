import requests
import json
import os
import random
from dotenv import find_dotenv, load_dotenv

# Environment variables
load_dotenv(find_dotenv())

# Client ID and Client Secret from the Spotify web dashboard portal from .env
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Client Credentials Flow Authorization URL
AUTH_URL = "https://accounts.spotify.com/api/token"

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

# Artist ID's from Kayne, Drake, and Kid Cudi
artist_id = ["3MZsBdqDrRTJihTHQrO6Dq","5eIbEEQnDM8yuDVB0bimSP","6l3HvQ5sa6mXTsMTB19rO5"]

# Random ID generator from the artist_id
random_choice = random.choice(artist_id)
# <iframe src="https://open.spotify.com/embed/artist/" width="100%" height="380" frameBorder="0" allowtransparency="true" allow="encrypted-media"></iframe>
# Auto populate the URI with artist_id URL
BASE_URL = "https://api.spotify.com/v1/artists/" + random_choice + "/top-tracks"

def get_spotify_data():
    params = {
        "country": "US"
    }

    response = requests.get(
        BASE_URL,
        headers=headers,
        params=params
    )

    # print(json.dumps(response.json(), indent=2))

    # Empty array to append song information and call in app.py
    song_info = []

    try:
        # Grab the song_name, artist_name, song_related_image, song_preview_URL

        # song_name
        song_name = json.dumps(response.json()['tracks'][0]['name'], indent=2)
        song_info.append(song_name.strip('"'))

        # artist_name
        artist_name = json.dumps(response.json()['tracks'][0]['album']['artists'][0]['name'], indent=2)
        song_info.append(artist_name.strip('"'))

        # song_related_image
        song_related_image = json.dumps(response.json()['tracks'][0]['album']['images'][0]['url'], indent=2)
        song_info.append(song_related_image.strip('"'))

        # song_preview_URL
        song_related_URL = json.dumps(response.json()['tracks'][0]['preview_url'], indent=2)
        song_info.append(song_related_URL.strip('"'))

        # # song_id to input into the genius API so that we can fetch both song data simultaneously.
        # song_id = json.dumps(response.json()['tracks'][0], indent = 2)
        # print(song_id)
        # song_info.append(song_id.strip('"'))
   
    except:
        print("Could not fetch song information!")

    return song_info

get_spotify_data()