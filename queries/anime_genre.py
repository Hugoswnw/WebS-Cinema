
#Usage example :
#  python queries/anime_genre.py raw_csv/anime_cleaned.csv > output_file.ttl

import csv
import sys

csvfile = open(sys.argv[1], 'r')
r = csv.reader(csvfile, delimiter=',')
r.next()
for row in r:
    for genre in row[28].split(", "):
        print '<https://myanimelist.net/anime/'+row[0]+'> <http://schema.org/genre> "'+genre+'"'
