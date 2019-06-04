# Install Tweepy and textblob - (pip install tweepy) & (pip install textblob)

import tweepy
from textblob import TextBlob

access_token = 'Access Token'
access_token_secret = 'Access Token Secret'
consumer_key = 'Consumer Key'
consumer_secret = 'Consumer Secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Kamala Harris')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	if analysis.sentiment[0]>0:
		print ('Positive')
	else:
		print ('Negative')
	print("")
