import pandas as pd

df = pd.read_csv('tweets2.csv')
print(df)

# displays just the time
tweet_time = df['created_at']
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']
print(tweet_clock_time)

