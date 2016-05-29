# Puzzle 2
# Do Men or Women take longer Hubway rides in Boston?
# By how many seconds? Round the answer DOWN to the nearest integer.
# Use the Hubway data from 2001-2013 at http://hubwaydatachallenge.org/

import pandas as pd

df = pd.DataFrame(pd.read_csv('hubway_trips.csv'))
mean = df.groupby('gender')['duration'].mean()

print df
print mean
print round(abs(mean[1] - mean[0]), 0)
