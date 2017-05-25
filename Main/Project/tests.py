#! /usr/bin/python3

import tweepy as tp
import sys
sys.path.append('/home/ben/Documents/Sensitive/twitter')
from twittercodes import *

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tp.API(auth, wait_on_rate_limit=True)

# public_tweets = api.home_timeline(include_rts=True, count=10)
# for tweet in public_tweets:
#     print(tweet.text)

print(dir(tp.StreamListener))

class listener(tp.StreamListener):

    def on_status(self, data):
        print(data)
        return True
    def on_status(self, status):
        print(status.text)

twitterStream = tp.Stream(auth, listener()) 
twitterStream.userstream(_with='user')