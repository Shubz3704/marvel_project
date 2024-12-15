import requests
import hashlib
import time
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

MARVEL_PUBLIC_KEY = os.getenv('MARVEL_PUBLIC_KEY')
MARVEL_PRIVATE_KEY = os.getenv('MARVEL_PRIVATE_KEY')
BASE_URL = "https://gateway.marvel.com:443/v1/public"

def generate_auth_params():
    """
    Generate the required timestamp and hash for Marvel API authentication.
    """
    ts = str(time.time())
    hash_md5 = hashlib.md5(f"{ts}{MARVEL_PRIVATE_KEY}{MARVEL_PUBLIC_KEY}".encode()).hexdigest()
    return {"ts": ts, "apikey": MARVEL_PUBLIC_KEY, "hash": hash_md5}

def fetch_character_by_id(character_id):
    """
    Fetch a character by their ID.
    """
    url = f"{BASE_URL}/characters/{character_id}"
    params = generate_auth_params()
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("data", {}).get("results", [])
    else:
        raise Exception(f"Error: {response.status_code} - {response.json()}")

def fetch_character_list(limit=20, offset=0, name=None):
    """
    Fetch a list of characters with optional filters.
    """
    url = f"{BASE_URL}/characters"
    params = generate_auth_params()
    params.update({"limit": limit, "offset": offset})
    if name:
        params["name"] = name
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("data", {}).get("results", [])
    else:
        raise Exception(f"Error: {response.status_code} - {response.json()}")
