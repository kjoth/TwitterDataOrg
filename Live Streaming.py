import tweepy
import json
from tweepy import OAuthHandler
# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'PbgT06xv4V6G7Hxxl6Q200s4j'
consumer_secret = '1tThxYhnxRKE6aMbS8IF7zk5yx5riXHC9RVp4FyRk0WxQ8FVn8'
access_token = '237610310-ky9IaPV1Eq59Jw9VPXBrbKQlvhi8RmAXI7bNLAeC'
access_secret = 'gKNp3T5KSXEZML3BZrGD2u9ggIaWYXPRuSlV5XnhTODCv'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

file_name = 'budget2017'
f = open(file_name + '.json', 'w', encoding='utf-8', errors="surrogateescape")

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        f.write(str(json.loads(data))+ '\n')
        print(data)
        
        #f.write(str(decoded))
		

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        #print('@%s: %s' % (decoded['created_at']['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
        #print( '')
        return True

    def on_error(self, status):
        print(status)
        return True # Don't kill the stream
        print("Stream restarted")

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    #print("Showing all new tweets for #Jayalaithaa:")

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
def start_stream():
    while True:
        try:
            stream = tweepy.Stream(auth, l)
            stream.filter(track=['#trump'])
        except: 
            continue
        
start_stream()
