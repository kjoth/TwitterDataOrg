# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 19:07:53 2016

@author: karthick.jothimani
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 17:15:26 2016

@author: karthick.jothimani
"""
# Import the necessary methods from "twitter" library
import os
import tweepy
import time

    
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

    # Variables that contains the user credentials to access Twitter API 
consumer_key = 'PbgT06xv4V6G7Hxxl6Q200s4j'
consumer_secret = '1tThxYhnxRKE6aMbS8IF7zk5yx5riXHC9RVp4FyRk0WxQ8FVn8'
access_token = '237610310-ky9IaPV1Eq59Jw9VPXBrbKQlvhi8RmAXI7bNLAeC'
access_token_secret = 'gKNp3T5KSXEZML3BZrGD2u9ggIaWYXPRuSlV5XnhTODCv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

get_user_to_query = '@MphasisCareers'

stuff = api.user_timeline(screen_name = '@Mphasiscareers', count=500, include_rts = True)

timestr = time.strftime("%Y%m%d-%H%M%S")
file_name = get_user_to_query +'_TweetData' + timestr
f = open(file_name + '.json', 'w', encoding='utf-8', errors="surrogateescape")

i = 0

for tweet in stuff:
    
    if tweet.lang == 'en':
        i=i+1
        print('Tweet Text: ' + str(tweet.text))
        print('tweet.coordinates: ' + str(tweet.coordinates))
        print('favorite_count: ' + str(tweet.favorite_count))
        print('retweet_count	: ' + str(tweet.retweet_count))
        print('retweeted	:' + str(tweet.retweeted))
        print('geo: ' + str(tweet.geo))
        print('id: ' + str(tweet.id))
        print('created_at	: ' + str(tweet.created_at))
        print('lang :' + str(tweet.lang))
        print('place :' + str(tweet.place))
        print('user: ' + str(tweet.user.name))
        print('contributors :' + str(tweet.contributors))
        
        f.write(str("Count: " + str(i)) + '\n')
        f.write(str("id \t:" + str(tweet.id)) + '\n')
        f.write(str("created_at \t:" + str(tweet.created_at)) + '\n')
        f.write(str("Tweet Text \t:" + str(tweet.text).replace('\r', ' ').replace('\n', ' ')) + '\n')
        f.write(str("tweet.coordinates \t:" + str(tweet.coordinates)) + '\n')
        f.write(str("favorite_count \t:" + str(tweet.favorite_count)) + '\n')
        f.write(str("retweet_count \t:" + str(tweet.retweet_count)) + '\n')
        f.write(str("retweeted \t:" + str(tweet.retweeted)) + '\n')
        f.write(str("user \t:" + str(tweet.user.name)) + '\n')
        f.write(str("geo \t:" + str(tweet.geo)) + '\n')
        f.write(str("lang \t:" + str(tweet.lang)) + '\n')
        f.write(str("place \t:" + str(tweet.place)) + '\n')
        f.write(str("contributors \t:" + str(tweet.contributors)) + '\n')
    
    #if hasattr(tweet, 'retweeted_status'):
         #print('Retweet original Author: ' + str(tweet.retweeted_status.author.screen_name))

         
    
    print('*' *40)
    
    
print(i)

f.close()
    
''' For the error
    print(tweet['text'])

TypeError: 'Status' object is not subscriptable

 http://stackoverflow.com/questions/216972/in-python-what-does-it-mean-if-an-object-is-subscriptable-or-not'''


