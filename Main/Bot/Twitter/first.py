import tweepy

consumer_key = 'TfD1r7iaAenrw7figv0X0WifD'
consumer_secret = 'fRUnw1zCPWPoj1BMv3GqN3A5Uw8Xoh1DfWxz2OVAtdEYNqOGOP'
access_token = 	'866663808441487360-OGyslHHAImLoRHAHPCrWc361gs1ZZjN'
access_token_secret = 'FsbSUvoFR29EDu8tA6hGzxsQf5c2zQpMU5zPgrSVz0hPN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status('test 2')