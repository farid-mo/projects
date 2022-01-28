# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 18:07:06 2022

@author: Farid
"""
import tweepy
import time

consumer_key = 'RPk72YWRWjYpiXtwAsukLZIxU'
consumer_secret = 'OiVHhnb8SaevlsSUOMqRUFZVdmilda8YTEoNHfuypBxUVI7hkH'
access_token = '1017497549995954176-ECKnDL9jDvpd4J4mwRTpKVqNbA8SgT'
access_token_secret = 'RsVtUmAIV9YqHf21bN0o7i6xLFUpg3To4NraqmEWVDyZ4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Print info about me
user = api.me()
print(f"Username: {user.name}")
print(f"Twitter handle:@{user.screen_name}")
print(f"No. of followers: {user.followers_count}")

# Print the home timeline
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

search_keyword = 'python'
n_tweets = 10

for tweet in tweepy.Cursor(api.search, search_keyword).items(n_tweets):
    try:
        tweet.favorite()
        print('I liked the tweet!')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# def limit_handler(cursor):
#     try:
#         while True:
#             yield cursor.next()
#     except tweepy.RateLimitError:
#         time.sleep(1000)


# Generous bot -> follow back
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)
#     # Follow back
#     # follower.follow()
