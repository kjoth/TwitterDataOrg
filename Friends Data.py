# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:04:05 2017

@author: Karthick.Jothimani
"""


def process_friends(friends,i):
    
    '''
    # Printing out put comment
  
    print("Count: " + str(i))    
    print("Following User ID \t: " + str(friends.id))
    print('Following name \t: ' + friends.name)
    print('Following Friends Count \t: ' + str(friends.friends_count))
    print("Following Tweets count \t:" + str(friends.statuses_count))
    print("Following Description \t:" + friends.description)
    print("Following Follower count \t:" + str(friends.followers_count))
    print("Following Created at \t:" + str(friends.created_at))
    print("Following Location \t:" + friends.location)
    print("verified USer  \t:" + str(friends.verified))
    print("screen name  \t:" + str(friends.screen_name))
    print("favourites or Likes count \t:" + str(friends.favourites_count))
    print("withheld incountries of USer  \t:" + str(friends.withheld_in_countries))
    '''
    #Writting into file
    f.write(str("Count: " + str(i)) + '\n')
    f.write(str("User ID \t: " + str(friends.id)) + '\n')
    f.write(str('Name \t: ' + str(friends.name)) + '\n')
    f.write(str("Description \t:" + str(friends.description).replace('\r', ' ').replace('\n', ' ')) + '\n')
    f.write(str("Created at \t:" + str(friends.created_at)) + '\n')
    f.write(str("Tweets count \t:" + str(friends.statuses_count)) + '\n')
    f.write(str("Follower count \t:" + str(friends.followers_count)) + '\n')
    f.write(str("Following count \t:" + str(friends.friends_count)) + '\n')
    f.write(str("Favourites count \t:" + str(friends.favourites_count)) + '\n')
    f.write(str("Following Location \t:" + str(friends.location)) + '\n')
    f.write(str("verified USer  \t:" + str(friends.verified)) + '\n')
    f.write(str("screen name  \t:" + str(friends.screen_name)) + '\n')
    f.write(str("time_zone \t: " + str(friends.time_zone) + '\n'))
    #f.write("*" * 40)
    
    
    '''
    if hasattr(friends, 'time_zone'):
        #print("User Time zone \t:", friends.time_zone)
        f.write(str("time_zone \: " + str(friends.time_zone) + '\n'))
        #print("User UTC Offset \t:" + str(friends.utc_offset))
        #print("User Status count \t:" + str(friends.statuses_count))
    else:
        f.write(str("Following time zone \t: NULL") + '\n')
    '''
    
    #if i == 208:
        #f.write('*' * 40)

consumer_key = 'PbgT06xv4V6G7Hxxl6Q200s4j'
consumer_secret = '1tThxYhnxRKE6aMbS8IF7zk5yx5riXHC9RVp4FyRk0WxQ8FVn8'
access_token = '237610310-ky9IaPV1Eq59Jw9VPXBrbKQlvhi8RmAXI7bNLAeC'
access_token_secret = 'gKNp3T5KSXEZML3BZrGD2u9ggIaWYXPRuSlV5XnhTODCv'

import sys
import os
#import jsonpickle
import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

get_user_to_query = '@MphasisCareers'

# Defining File with Date and Time Stamp attached
timestr = time.strftime("%Y%m%d-%H%M%S")
file_name = 'MphasisCareers_friends' + timestr
f = open(file_name + '.json', 'w', encoding='utf-8', errors="surrogateescape")

user_friends_count = api.get_user(get_user_to_query).friends_count

# Code for printing the count of freinds
#print(str(user_friends_count) + '\n')
#print('\n')
#print('*'* 50 + '\n')

# Storing the cursor data in the "user_friends_count" variable
user=tweepy.Cursor(api.friends, id = get_user_to_query).items()

i=1


try:
    for friends in user:
        process_friends(friends, i)
        time.sleep(1)   #Code for sleeping teh script to avoid the connection error
        i=i+1
        if i%100==0:
            #time.sleep(600)  #Code for sleeping the script to avoid the connection error at the end of 100 fetches
            print("sleeping")
            #print(friends.name)   #Code for verifying the process of fetching the friends
            
except Exception as e:
    print(e)
    f.write(str(str(e) + '\n'))
    time.sleep(600)  #Code for letting the script sleep for 10 minutes due to connection errors
    

f.close()


