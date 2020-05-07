# Runs alarm.mp3 when the aamc_mcat twitter account updates

import tweepy
import keys
from datetime import datetime
import time
import os


auth=tweepy.OAuthHandler(keys.consumer_key, keys. consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api=tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
aamc = api.get_user('aamc_mcat')

initial=aamc.status.text
print(initial)


def mcat_wait():
    interval = 1.
    next_t = time.time()
    while(datetime.now().hour < 12):
        if aamc.status.text != initial:
            os.system('alarm.mp3')
            print('Sign up fool')
            break
        else:
            next_t += interval
            time.sleep(next_t - time.time())


mcat_wait()
