# Script to automatically follow Spotify artists by their Spotify IDs
#
# Requirements:
#	Python 3
#	tidalapi (pip install tidalapi)
#
# Usage:
#	- Replace TIDAL_USERNAME and TIDAL_PASSWORD with values for your user account
#	- create file artists.txt in same folder as this python script consisting
#	of one artist name per line
#	- run ./tidal_follow_artists.py

import csv
import sys
import pprint
import time

import tidalapi

TIDAL_USERNAME=''
TIDAL_PASSWORD=''
artist_names = []

file = open("artists.txt", "r",  encoding="utf8") 

for line in file:
    artist_names.append(line.rstrip())

session = tidalapi.Session()
session.login(TIDAL_USERNAME, TIDAL_PASSWORD)
favorites = tidalapi.Favorites(session, session.user.id)

for artist_name in artist_names:
    artist_data = session.search('artist', artist_name)

    if len(artist_data.artists) == 0:
        print('WARNING: No artist found for {}, continuing'.format(artist_name))
        continue

    favorites.add_artist(artist_data.artists[0].id)
    print('Added {}'.format(artist_name))
    time.sleep(2)