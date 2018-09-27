import csv
import sys
import pprint

import tidalapi

session = tidalapi.Session()
session.login('login', 'password')
favorites = tidalapi.Favorites(session, session.user.id)

with open('myplaylist.csv', encoding="utf8") as csvfile:
	rows = csv.reader(csvfile)
	for artist, track in rows:
		print('Processing {} - {}\n'.format(artist, track))
		
		albums_data = session.search('track', '{} - {}'.format(artist, track)).albums

		if len(albums_data) == 0:
			print('WARNING: No albums found for {} - {}, continuing'.format(artist, track))
			continue

		selection = 0

		album_to_add = albums_data[selection]
		favorites.add_album(album_to_add.id)

		print('\n{}\n'.format('*' * 20))