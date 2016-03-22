'''
Created on Apr 4, 2014

@author: bonino

Copyright (c) 2014 Dario Bonino

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
'''



import tts, urllib, time
from twitter import *

def getTweets(hashtag):
    # get access to apis

    tw = Twitter(
    auth=OAuth(consumer_key='wIDHvofdfV2QO94s1bjebQ',
                      consumer_secret='nO0q0Ko8EBQ6Lb8FNLwEsT3r2QLkjWsO02dr9uegU',
                      token='2408639030-qbEH2eTP5Qc0fJU9NfhDRREBB9F44cxhGSFbV3T',
                      token_secret='xPLGzRWpsPeXCFzw6PI98K91XegwKAFFq0JPjgTJRj6ge'))


    results = tw.search.tweets(q="#"+hashtag)


    tweets = []

    for status in results['statuses']:
        print status
        tweets.append(status['text'])

    return tweets

def sayTweets(tweets = None):
    '''Says tweets
    Args: a list containing the found statuses
    '''
    if(tweets!=None):
            #iterate over tweets
            for tweet in tweets:
                # remove the non-ascii characters
                text = tweet.encode('ascii', 'replace')
                #read the status text
                tts.say(urllib.quote_plus(text),'en')
                time.sleep(2)


if __name__ == '__main__':
    hashtag = raw_input('hashtag: ')

    #fetch tweets
    tweets = getTweets(hashtag)
    #read tweets
    sayTweets(tweets)





'''
consumer key: wIDHvofdfV2QO94s1bjebQ
consumer secret: nO0q0Ko8EBQ6Lb8FNLwEsT3r2QLkjWsO02dr9uegU
access token: 2408639030-qbEH2eTP5Qc0fJU9NfhDRREBB9F44cxhGSFbV3T
access token secret: xPLGzRWpsPeXCFzw6PI98K91XegwKAFFq0JPjgTJRj6ge

'''