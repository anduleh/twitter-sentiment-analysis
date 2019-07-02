import tweepy
from textblob import TextBlob
import keys

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

