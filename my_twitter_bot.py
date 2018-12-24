import tweepy

print('this is my twitter bot')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCES_KEY = ''
ACCES_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCES_KEY, ACCES_SECRET)
api = tweepy.API(auth)
