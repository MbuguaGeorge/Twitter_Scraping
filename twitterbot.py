import tweepy
import sys


consumerkey = "BOLQwKdfnW50TlLovyBwcuqLA"
consumerSecret = "KNPKXK0nO2L7FwTEwK4nHqJJsAX5pCY8pfOTXGO32cZwcUiUgg"
accessToken = "1154337206875693056-sUaGCmzkcN9jLZr39JY4EyYWzlsNbv"
accessTokenSecret = "IystYocSsxxBYOykVY5W6mjVdG1KLPrcg3chMqPkg1T85"

auth = tweepy.OAuthHandler(consumerkey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

keyword = input("Enter Tweet To Search: ")
noOfTweets = int(input("How Many Tweets To Analyze: "))

tweets = tweepy.Cursor(api.search, q= keyword, tweet_mode='extended', include_rts=False).items(noOfTweets)


def save_tweet(T):
    T = input("do you want to save tweet? ")
    if T == ("yes") or T == ("Yes") or T == ("YES"):
        result = input("enter username of tweet to save: ")
        return result
    elif T == ("no") or T == ("No") or T == ("NO"):
        sys.exit()
    else:
        print("invalid")
        
UserID='result'
tweet = api.user_timeline(screen_Name=UserID, count=20)

for info in tweets[3]:
    print('ID: {}'.format(info.id))
    print(info.created_at)
    print(info.full_text)
    print("\n")
    