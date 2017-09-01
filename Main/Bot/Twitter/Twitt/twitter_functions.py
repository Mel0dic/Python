import twitter, util, sys
sys.path.append('../../../../Sensitive')
from twitter_codes import *

BOSTON_WOEID = 2367105

api = twitter.Api(consumer_key=key,consumer_secret=secret,access_token_key=access_key,access_token_secret=access_secret)

def search(searchTerm):
    """
    Print recent tweets containing `searchTerm`.

    To test this function, at the command line run:
        python twitter_api.py --search=<search term>
    For example,
        python twitter_api.py --search=python
    """
    api = twitter.Api(consumer_key=key,consumer_secret=secret,access_token_key=access_key,access_token_secret=access_secret)
    tweets = api.GetSearch(searchTerm)
    for tweet in tweets:
        util.safe_print(tweet.GetText())

def trendingTopics():
    """
    Print the currently trending topics.

    To test this function, at the command line run:
        python twitter_api.py -t
    """
    api = twitter.Api(consumer_key=key,consumer_secret=secret,access_token_key=access_key,access_token_secret=access_secret)
    trending_topics = api.GetTrendsWoeid(BOSTON_WOEID)
    for topic in trending_topics:
        util.safe_print(topic.name)

def userTweets(username):
    """
    Print recent tweets by `username`.

    You may find the twitter.Api() function GetUserTimeline() helpful.

    To test this function, at the command line run:
        python twitter_api.py -u <username>
    For example,
        python twitter_api.py -u bostonpython
    """
    pass

def trendingTweets():
    """
    Print tweets for all the trending topics.

    To test this function, at the command line run:
        python twitter_api.py -w
    """
    pass
