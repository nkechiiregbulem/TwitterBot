import tweepy

access_token = 'access token'
access_token_secret = 'access token secret'
consumer_key = 'consumer key'
consumer_secret = 'consumer secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

def main():
    search = ("bitcoin")
    
    numberofTweets = 5
    for tweet in tweepy.Cursor(api.search, search).items(numberofTweets):
        try:
            tweet.favorite()
            print("Tweet Favorited")
        except tweepy.TweetError as e:
            print(e.reason)
        except StopIteration:
            break

main()
