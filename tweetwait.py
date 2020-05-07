# Runs alarm.mp3 when the chosen twitter account updates

import tweepy
import keys
from datetime import datetime
import time
import os


auth=tweepy.OAuthHandler(keys.consumer_key, keys. consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api=tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
name = input('Enter twitter account: ')
account = api.get_user(name)

initial=aamc.status.text
print(initial)


def tweet_wait():
    interval = 1.
    next_t = time.time()
    while(datetime.now().hour < 12):
        if account.status.text != initial:
            os.system('alarm.mp3')
            break
        else:
            next_t += interval
            time.sleep(next_t - time.time())


mcat_wait() 
