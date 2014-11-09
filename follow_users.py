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
#users to add
i = 0

for item in y:
	try:
		print item
		api.create_friendship(item)
		print '\n'
		time.sleep(3)
		i += 1
		if i%100==0:
			time.sleep(100) 
	except:
		print "break"
