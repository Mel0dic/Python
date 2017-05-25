#! /usr/bin/python3

import tweepy as tp
import sys
sys.path.append('/home/ben/Documents/Sensitive/twitter')
from twittercodes import *

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tp.API(auth, wait_on_rate_limit=True)

something = api.get_status(867002900568002561)

print('\n\n')
print(dir(something.author))
print(something.author.time_zone)