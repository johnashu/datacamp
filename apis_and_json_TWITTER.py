import json
import re

import pandas as pd
import tweepy

from twitter_api_cred import (access_token, access_token_secret, consumer_key,
                              consumer_secret)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file_name = 'tweets.txt'

    def on_status(self, status):
        tweet = status._json
        with open(self.file_name, 'a') as file:
            file.write(json.dumps(tweet) + '\n')
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False

    def on_error(self, status):
        print(status)


def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False


l = MyStreamListener()

stream = tweepy.Stream(auth, l)

stream.filter(track=['brexit'])

tweets_data_path = 'tweets.txt'

tweets_data = []

tweets_file = open(tweets_data_path, 'r')

for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()

df = pd.DataFrame(tweets_data, columns=['text', 'lang'])
print(df.head())

[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

print([clinton, trump, sanders, cruz])


import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

cd = ['clinton', 'trump', 'sanders', 'cruz']

ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
