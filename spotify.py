import requests
import json
import os
import random
from dotenv import find_dotenv, load_dotenv

# Environment variables
load_dotenv(find_dotenv())

# Client ID and Client Secret from the Spotify web dashboard portal from .env

# Client Credentials Flow Authorization URL
AUTH_URL = "https://accounts.spotify.com/api/token"

# Post request to generate authorization token
auth_response = requests.post(AUTH_URL, {
    "grant_type": "client_credentials",
    "client_id": os.getenv('CLIENT_ID'),
    "client_secret": os.getenv('CLIENT_SECRET')
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

def get_spotify_data():
    BASE_URL = "https://api.spotify.com/v1/artists/" + random_choice + "/top-tracks"

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
   
    except:
        print("Could not fetch song information!")

    return song_info

artist_name_genius = get_spotify_data()[1]

# Client Credentials Flow Authorization URL
CLIENT_ACCESS_TOKEN = os.getenv('CLIENT_ACCESS_TOKEN')

# Import the auth token into the Authorization key header
headers_genius = {
    'Authorization': f'Bearer {CLIENT_ACCESS_TOKEN}'
}

BASE_URL_genius = "http://api.genius.com/search?q=" + artist_name_genius + "?"

r = requests.get(
    BASE_URL_genius,
    headers=headers_genius
)

def get_genius_data():
    genius_url = []
    genius_url.append(r.json()['response']['hits'][0]['result']['url'])
    return genius_url

def get_spotify_artist_info(artist_id):
    BASE_URL = f"https://api.spotify.com/v1/artists/{artist_id}"

    response = requests.get(
        BASE_URL,
        headers=headers
    )
    # ['name']
    response = response.json()

    return response

def get_spotify_data_rand(artist_id):
    BASE_URL = "https://api.spotify.com/v1/artists/" + artist_id + "/top-tracks"

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
   
    except:
        print("Could not fetch song information!")

    return song_info