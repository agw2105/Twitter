import tweepy
from tweepy import OAuthHandler
import json

consumer_key = 'key'
consumer_secret = 'secret'
access_token = 'token'
access_secret = 'access secret'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


query = '#Hashtag'
search = api.search(q = query)

users = []
for item in search:
    users.append(item.author._json['screen_name'])

users.to_csv("users.csv")