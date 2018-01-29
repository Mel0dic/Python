import tweepy, sys
sys.path.append('../../../../Sensitive')
from twitter_codes import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status('test 2')