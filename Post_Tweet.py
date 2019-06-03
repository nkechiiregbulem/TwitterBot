#Install TwitterAPI - pip install TwitterAPI

from TwitterAPI import TwitterAPI

access_token = "Access Token"
access_token_secret = "Access Token Secret"
Consumer_Key = "Consumer Key"
Consumer_Secret = "Consumer Secret"


api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

r = api.request('statuses/update', {'status':'Insert your tweet'})
print(r.status_code)

#Status code should be returned as 200 or 403
