import time
import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
# @Twitter Handle

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

y = []
#add list of users to be deleted (can also do with CSV file.write)
deleted = []

for item in y:
	try:
		print item
		api.destroy_friendship(item)
		deleted.extend(item)
		time.sleep(.5)
	except:
		print "break"