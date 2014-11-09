import time
import tweepy
from datetime import datetime

f = open("output.txt","w")

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
# @Twitter Handle


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="").pages():
	#screen_name = "" : input handle you want to get users from
    ids.extend(page)
    datetime.now().time()
    print ids
    print len(ids)
    if len(page) == 5000:
    	time.sleep(1)

ids = str(ids)
f.write(ids)
f.close()
