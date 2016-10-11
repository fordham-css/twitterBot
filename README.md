#twitterBot
twitterbot, optionally with gmail integration

##Required Libraries

To use the basic twitter bot, you must install the python-twitter library
`<pip install python-twitter>`

To use tha advanced bot, with gmail integration, you must install the python gmail library
`<pip install google-api-python-client>`

##Required Files
* `<twitter_auth.py>`: a python file which contains all twitter keys and tokens for your python API an example can be seen in auth_example.py
* `<google_auth.py>`: a python file, chich contains `<user_ID = 'your@email'>` (only needed for advanced bot)
* `<client_secret.json>`: a JSON file, given to you when you register for you google app. 
* `<storage.json>`: a JSON file, shoud be created when you first run the advanced bot
