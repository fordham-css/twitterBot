#requires python-twitter
	#pip install python-twitter
import twitter

#requires auth.py, which holds all keys and tokens
from twitter_auth import *

#uses the keys to connect to the twitter API
api = twitter.Api(consumer_key= Consumer_Key,
					consumer_secret= Consumer_Secret,
					access_token_key= Access_Token,
					access_token_secret= Access_Secret)

#Posts the update
status = api.PostUpdate("My First Bot Post!")

#prints the update to the screen
print(status.text)
