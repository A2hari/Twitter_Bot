import tweepy
import time

CONSUMER_KEY ="NM4m0iQZlA41wvgq2kzc1MmuM"
CONSUMER_SECRET = "D7czHFGNJnKpaQiI53OJmB0zBeYts3FklCAxZWIJcxx3M0iUXo"
ACCESS_KEY ="904197019866038272-V0XmpQKSq424GYcpDglr0J9OUAzvdAQ"
ACCESS_SECRET="agICq0bdNZmUvu27Ov3uu27LMipTQ616hsLZJW77YgD6y"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file = "last_tweet_id.txt"

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

while True:
    reply_to_tweets()
    time.sleep(6)
