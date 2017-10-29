#coding=utf-8
import json
import threading
import tweepy
from time import ctime,sleep
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = CK
consumer_secret = CS
access_token = AK
access_secret = AS

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweetCount = 50


def gettimeline(screen_name):
    print 'get timeline of tweet'
    results = api.user_timeline(id = screen_name, count = tweetCount)
    for tweet in results:
        try:
            if tweet.lang == 'en':
                f.write(json.dumps(tweet._json)+'\n')
        except BaseException as e:
            print('Error on_data:'+str(e))

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            f = open('crawler1.json','a')
            jsontype = json.loads(data)
            s_name = jsontype['user']['screen_name']
            if jsontype['lang']=='en':
                if jsontype['geo'] != None:
                    print 'get one'
                    gettimeline(s_name)
            f.close()
        except BaseException as e:
            print('Error on_data:'+str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#maccas', '#McDonald', '#kfc', '#dominos', '#subway', '#nandos', '#pizza hut','fastfood','fast food', 'carry-out',
                             'eat in', 'drive through', 'franchise', 'menu', 'combo', 'nutrition', 'beverage', 'soft drink', 'fountain drink',
                             'slushie', 'smoothie', 'coffee', 'sub', 'bun', 'muffin', 'scone', 'biscuit', 'sides', 'condiments', 'dressing',
                             'fries', 'hash browns', 'onion rings', 'burger', 'chicken', 'sausage', 'hotdog', 'bacon', 'beef'])
