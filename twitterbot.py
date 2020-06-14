import tweepy
import sys
import csv
import time


consumerkey = "xxxxxxxxxxxxxxxxxxxxxxx"
consumerSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
accessToken = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
accessTokenSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

auth = tweepy.OAuthHandler(consumerkey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


keyword = input("Enter Tweet To Search: ")
noOfTweets = int(input("How Many Tweets To Analyze: "))

tweets = tweepy.Cursor(api.search, q= keyword, tweet_mode="extended").items(noOfTweets)

for tweet in tweets:
    print(tweet.full_text)

def save_tweet(T):
    T = input("do you want to save tweet? ")
    if T == ("yes") or T == ("Yes") or T == ("YES"):
        print('saving')
    elif T == ("no") or T == ("No") or T == ("NO"):
        sys.exit()
    else:
        print("invalid")

save_tweet('T')

def extract_tweets(userID):
    alltweets = []
    new_tweets = api.user_timeline(screen_name=keyword, count=200, include_rts=False, tweet_mode='extended')
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    outtweets = [
        [tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8"), 1 if 'media' in tweet.entities else 0,
         1 if tweet.entities.get('hashtags') else 0, tweet.retweet_count]
        for tweet in alltweets]
    with open('TWEETS.csv', mode='a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)
    pass

extract_tweets('userID')