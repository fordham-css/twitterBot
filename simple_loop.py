#requires python-twitter
	#pip install python-twitter
import twitter
import time
#requires auth.py, which holds all keys and tokens
from twitter_auth import *


count = 1
while True:
	#uses the keys to connect to the twitter API
	api = twitter.Api(consumer_key= Consumer_Key,
						consumer_secret= Consumer_Secret,
						access_token_key= Access_Token,
						access_token_secret= Access_Secret)
	
	count += 1	
	#Posts the update
	status = api.PostUpdate("Post from server number:" + str(count))
	
	#prints the update to the screen
	print(status.text)
	time.sleep(60)
