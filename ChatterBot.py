# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "fkxBgq9L4nHMvZOh8sJgWhPxI"
consumer_secret = "4vbR5Pc69sHkD2rRt4BySnKoknx2YfAr3U3RRKnPhqatISZi8D"
access_token = "2697326256-8rbvcf2wW0JSdcuS3cyZf6DO8odMbnW5geqytCS"
access_token_secret = "UEpJXymFPkKZmoanJRVMURa4DodWzaDgZpWY2bLAmIKTd"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    tweet_text = "Can't stop. Won't stop. Chatting! This is Tweet #{}!".format(tweet_number)
    try:
        api.update_status(tweet_text)
    except Exception as e:
        print(e)
        print("Attempted to tweet: {}".format(tweet_text))


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(10)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1
