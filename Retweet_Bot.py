# First install Tweepy - pip install tweepy


import tweepy

consumer_key = "Consumer Key"
consumer_secret = "Consumer Secret"
access_token = "Access Token"
access_token_secret = "Access Token Secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

def main():
    search = ("downlighting")
    
    numberofTweets = 5
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweetError as e:
            print(e.reason)
        except StopIteration:
            break
main()
