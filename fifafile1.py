# fifa 1 using pandas

import statistics
import pandas


df = pandas.read_csv('FIFA21-player-list.csv')

clubName = df['club_name']

print(clubName)