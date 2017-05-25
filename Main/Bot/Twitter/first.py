import tweepy
import sys
sys.path.append('/home/ben/Documents/Sensitive/twitter')
from twittercodes import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status('test 2')