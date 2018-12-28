import tweepy           #library  for building apps for twitter
import time            #library for controling the sleep of the message

CONSUMER_KEY ="Enter your api key"   
CONSUMER_SECRET = "Enter your api secret key"
ACCESS_KEY ="Enter your access key"
ACCESS_SECRET="Enter your access secret key"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file = "last_tweet_id.txt"           #linking the file which stores the last tweet id

def read_last_id(file):
        file_read = open(file,'r')
        last_id = file_read.read()
        file_read.close()
        return int(last_id)


def write_last_id(file,last_tweet_id):
        file_write=open(file,'w')
        file_write.write(last_tweet_id)
        file_write.close()
        return
def reply_to_tweets():
    print("rerieving and replting to the tweets......",flush=True)
    last_tweet_id=read_last_id(file)
    mentions =api.mentions_timeline(last_tweet_id,tweetmode="extended",flush=True)
    for mention in reversed(mentions):
          print(str(mention.id)+" "+mention.text,flush=True)
          last_tweet_id=str(mention.id)
          write_last_id(file,last_tweet_id)
          if "#helloworld" in mention.text.lower():   
              print("found Hello world!\nWaving you back user ......",flush=True)
              api.update_status("@"+mention.user.screen_name+" "+"Hello world waving back to you !",mention.id)
          if "#hello" in mention.text.lower():
              print("found hello \nWaving you back user ......",flush=True)
              api.update_status("@"+mention.user.screen_name+" "+"Hello buddy waving back  you !",mention.id)
          if "#test" in mention.text.lower():
              print("matching content found \nWaving you back user ......",flush=True)
              api.update_status("@"+mention.user.screen_name+" "+"this is a bot replyed to the tweet successfully",mention.id)

while True:                   #infinite loop
    reply_to_tweets()
    time.sleep(6)               
