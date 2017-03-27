# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:29:12 2017

@author: Karthick.Jothimani
"""

def process_followers(followers,i):
    
    '''
    # Printing out put comment
  
    print("Count: " + str(i))    
    print("Followers User ID \t: " + str(followers.id))
    print('Followers name \t: ' + followers.name)
    print('Followers Friends Count \t: ' + str(followers.friends_count))
    print("Followers Tweets count \t:" + str(followers.statuses_count))
    print("Followers Description \t:" + followers.description)
    print("Followers Follower count \t:" + str(followers.followers_count))
    print("Followers Created at \t:" + str(followers.created_at))
    print("Followers Location \t:" + followers.location)
    print("verified USer  \t:" + str(followers.verified))
    print("screen name  \t:" + str(followers.screen_name))
    print("favourites or Likes count \t:" + str(followers.favourites_count))
    print("withheld incountries of USer  \t:" + str(followers.withheld_in_countries))
    '''
    #Writting into file
    f.write(str("Count: " + str(i)) + '\n')
    f.write(str("User ID \t: " + str(followers.id)) + '\n')
    f.write(str('Name \t: ' + str(followers.name)) + '\n')
    #f.write(str("Description \t:" + str(str(followers.description).replace('\r', ' ').replace('\n', ' ')) + '\n')
    f.write(str("Description \t:" + str(followers.description).replace('\r', ' ').replace('\n', ' ')) + '\n')
    f.write(str("Created at \t:" + str(followers.created_at)) + '\n')
    f.write(str("Tweets count \t:" + str(followers.statuses_count)) + '\n')
    f.write(str("Follower count \t:" + str(followers.followers_count)) + '\n')
    f.write(str("Following count \t:" + str(followers.friends_count)) + '\n')
    f.write(str("Favourites count \t:" + str(followers.favourites_count)) + '\n')
    f.write(str("Location \t:" + str(followers.location)) + '\n')
    f.write(str("verified USer  \t:" + str(followers.verified)) + '\n')
    f.write(str("screen name  \t:" + str(followers.screen_name)) + '\n')
    f.write(str("time_zone \t: " + str(followers.time_zone) + '\n'))
    #f.write("*" * 40)

    '''
    if hasattr(followers, 'time_zone'):
        #print("followers Time zone \t:", followers.time_zone)
        f.write(str("time_zone \: " + str(followers.time_zone) + '\n'))
        #print("followers UTC Offset \t:" + str(followers.utc_offset))
        #print("followers Status count \t:" + str(followers.statuses_count))
    else:
        f.write(str("Followers time zone \t: NULL") + '\n')
        
    #if i == 208:
        #f.write('*' * 40)
    '''

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

get_user_to_query = '@Mphasis'

# Defining File with Date and Time Stamp attached
timestr = time.strftime("%Y%m%d-%H%M%S")
file_name = get_user_to_query +'_followers' + timestr
f = open(file_name + '.json', 'w', encoding='utf-8', errors="surrogateescape")

# Storing the cursor data in the "user_followers_count" variable
user_followers_count = api.get_user(get_user_to_query).followers_count

# Code for printing the count of followers
#print(str(user_followers_count) + '\n')
#print('\n')
#print('*'* 50 + '\n')

user=tweepy.Cursor(api.followers, id = get_user_to_query).items()

i=1

try:
    for followers in user:
        process_followers(followers, i)
        time.sleep(5)   #Code for sleeping teh script to avoid the connection error
        i=i+1
        if i%100==0:
            #time.sleep(600)  #Code for sleeping the script to avoid the connection error at the end of 100 fetches
            print("sleeping")
            #print(followers.name)   #Code for verifying the process of fetching the followers
            
except Exception as e:
    print(e)
    f.write(str(str(e) + '\n'))
    time.sleep(600)  #Code for letting the script sleep for 10 minutes due to connection errors
    

f.close()


