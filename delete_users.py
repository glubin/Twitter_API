import time
import tweepy

f = open("deleted.txt","w")
s = open("idsDeleted.txt","w")

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
# @Twitter Handle

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

y = []
deleted = []

for item in y:
	try:
		print item
		api.destroy_friendship(item)
		deleted.extend(item)
		time.sleep(.5)
	except:
		print "break"

ids = str(ids)
print ids
f.write(ids)
f.close

y = str(y)
s.write(y)
s.close