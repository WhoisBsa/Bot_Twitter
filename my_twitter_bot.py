import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.


# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
print('this is my twitter bot', flush=True)

CONSUMER_KEY = 'o4NSc2RLeZsjxu6G5Bz2XYs7T'
CONSUMER_SECRET = 'vsGyYjBHIsAr8I5V6yN4lrja7YlIgUtNbooSFEl0BVmx3hHjnv'
ACCESS_KEY = '1077269677884215298-HtNubmmCEGqLxsms4Tm93fJWYoylvw'
ACCESS_SECRET = '1bs3rYXF6BJjnNHfJebF72kemCCzClNwBBsQYm3xActRO'	

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrievind and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + '-' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('Found helloworld!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + 
                '#HelloWorld de volta pra você!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)