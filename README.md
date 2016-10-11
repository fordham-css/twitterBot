#twitterBot
twitterbot, optionally with gmail integration

##Required Libraries

*`pip install python-twitter`: To use the basic twitter bot, you must install the python-twitter library

*`pip install google-api-python-client`: To use tha advanced bot, with gmail integration, you must install the python gmail library


##Required Files
* `twitter_auth.py`: A python file which contains all twitter keys and tokens for your python API an example can be seen in auth_example.py
* `google_auth.py`: A python file, chich contains `<user_ID = 'your@email'>` and the querry you would like to search for (only needed for advanced bot)
* `client_secret.json`: A JSON file, given to you when you register for you google app. 
* `storage.json`: A JSON file, shoud be created when you first run the advanced bot
