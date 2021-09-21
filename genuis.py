import requests
import json
import os
import random
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv)

CLIENT_ID = os.getenv('CLIENT_ID_genius')
CLIENT_SECRET = os.getenv