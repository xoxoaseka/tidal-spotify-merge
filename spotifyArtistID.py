# Script to convert music artist names to Spotify IDs
#
# Requirements:
#	Python 3
#	spotipy (pip install spotipy)
#
# Usage:
#	- Replace SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
#	with values for your app (you can get these from Spotify API page)
#	- replace username variable with your username
#	- create file artists_plain.txt in same folder as this python script consisting
#	of one artist name per line (ex. The Prodigy)
#	- run ./spotify_convert_artists.py
#	- after finishing you'll find a new file artist_converted.txt with spotify IDs
#	in same folder as script

import spotipy
import sys
import pprint

import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2

SPOTIPY_CLIENT_ID=''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI=''
username = '' 
scope = 'user-library-modify'

token = util.prompt_for_user_token(
    username=username,
    scope=scope,
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI
)

sp = spotipy.Spotify(auth=token)

file = open("artists_plain.txt", "r",  encoding="utf8") 

for line in file:
    with open("artists_converted.txt", "a") as myfile:
        result = sp.search(line, limit=1, type='artist')
		
        if result['artists']['items']:
            myfile.write(result['artists']['items'][0]['id'] + "\n")