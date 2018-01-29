#! /usr/bin/python3

import tweepy as tp
import sys
sys.path.append('/home/ben/Documents/Sensitive/twitter')
from twittercodes import *

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tp.API(auth, wait_on_rate_limit=True)

class MyStreamListener(tp.StreamListener):
    def on_status(self, status):
    	if not status.retweeted:
    		print(status.text)

myStreamListener = MyStreamListener()
myStream = tp.Stream(auth = api.auth, listener=myStreamListener, retweets=False)

myStream.filter(track=['#GE2017'])
