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


def auto():
    query = ("Amazon", "Tax", "Profit")
    
    language = "en"
    
    results = api.search(q=query, lang=language)
    
    for tweet in results:
        print(tweet.user.screen_name,"Tweeted:",tweet.text)
        
auto()
