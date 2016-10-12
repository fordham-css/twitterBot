#gmail imports
from __future__ import print_function
import httplib2
import os


from apiclient import discovery
from oauth2client import client, tools
from oauth2client.file import Storage

#Twitter imports
import twitter
from twitter_auth import *

#other imports
import json
import time

#get variable for gmail
	#gives us user_ID
from google_auth import *

#gmail boilerplate
try:
	import argparse
	flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
	flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.modify'		# If modifying these scopes, delete your previously saved credentials
CLIENT_SECRET_FILE = 'client_secret.json'					# at ~/.credentials/gmail-python-quickstart.json
APPLICATION_NAME = 'CSS Gmail / TwitterBot Integration'


#my function
#takes in a string, and posts it to twitter
#requires auth.py, which holds all keys and tokens
def tweet(post):
	api = twitter.Api(consumer_key= Consumer_Key,
					consumer_secret= Consumer_Secret,
					access_token_key= Access_Token,
					access_token_secret= Access_Secret)

	status = api.PostUpdate(post)	

#gmail boilerplate
#connects you to gmail
def get_credentials():
	"""Gets valid user credentials from storage.

	If nothing has been stored, or if the stored credentials are invalid,
	the OAuth2 flow is completed to obtain the new credentials.

	Returns:
		Credentials, the obtained credential.
	"""
	home_dir = os.path.expanduser('~')
	credential_dir = os.path.join(home_dir, '.credentials')
	if not os.path.exists(credential_dir):
		os.makedirs(credential_dir)
	credential_path = os.path.join(credential_dir,'gmail-python-quickstart.json')

	store = Storage(credential_path)
	credentials = store.get()
	if not credentials or credentials.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
		flow.user_agent = APPLICATION_NAME
		if flags:
			credentials = tools.run_flow(flow, store, flags)
		else: # Needed only for compatibility with Python 2.6
			credentials = tools.run(flow, store)
		print('Storing credentials to ' + credential_path)
	return credentials

#gets the subjects to be tweeted
#uses get_credentials()
def get_subjects():
	#signs into gmail
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('gmail', 'v1', http=http)

	# gets contense of the inbox
		#future update: userId could be "me", if we want to integrate other emails at some point.
	response = service.users().messages().list(userId=user_ID, q=search_querry).execute()

	#goes through inbox, and expands (gets more info) on each email
	messages = []
	if 'messages' in response:
		messages.extend(response['messages'])

	#gets the next page, if the inbox is more than one page
		#not needed, the inbox should never be more than one page.
	while 'nextPageToken' in response:
		page_token = response['nextPageToken']
		response = service.users().messages().list(userId=user_ID, q=search_querry, pageToken=page_token).execute()
		messages.extend(response['messages'])

	#not clean. Declare somewhere else.
	subjects = []

	try:
		for message in response['messages']:


			entire_message = service.users().messages().trash(userId=user_ID, id=message['id']).execute()	#gets the message
			subject2Tweet = entire_message['payload']['headers'][17]['value']	#goes through the message to find the subject. Not really futureproof, could be expanded.

			subjects.append(subject2Tweet)
		print("Printing Subjects")

	except KeyError:
		print("No Messages")


	return subjects

#main function, ran at start, and controls the entire program.
def main():

	shouldTweet=True

	while True:
		subjects = get_subjects()
		for value in subjects:
			tweet(value)

		#tweets before a meeting
		gmt_time = time.gmtime()
		if gmt_time[6]==2 and gmt_time.tm_hour == 22 and shouldTweet:
			tweet("Have fun at the CSS meeting tonight") #should we tweet @CSS
			shouldTweet= False

		if gmt_time[6]==3:
			shouldTweet=True
		

		time.sleep(30)


#starts the program
if __name__ == '__main__':
	main()
