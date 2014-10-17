import sys
import json
from collections import defaultdict

# Function to collect tweets from the text file.
def collectTweets(f):
    data  = [ ]
    for line in f:
        data.append(json.loads(line,encoding = 'UTF-8'))
    tweets = [ ]
    count = 0
    while (count < len(data)):
        tweets.append(data[count].get('text'))
        count = count + 1
    return tweets

# Need a fucntion to store the scores into a list or dictionary or tuples.
# Argument 'tweets'

def displayScore(tweetsall):
    tweetnumber = 0
    tweetscore = defaultdict(list)
    termfreq = {'':(0,0)}
    # termcount = {'':0}
    for tweetnumber in range(len(tweetsall)):
        tweetscore.update(calculateFrequency(tweetsall[tweetnumber],termfreq))
        tweetnumber = tweetnumber +1
    # print tweetscore
    tweetscore.pop('')
    words = tweetscore.keys()
    alloccur = float(sum(tweetscore.values()))
    for w in words:
        #print(tweetscore[w])
        freq = float(tweetscore[w]/alloccur)
        print  w , ' ', freq




# Calculate score function which need a tweet s an input so that it can compute the score.

def calculateFrequency(tweet,termfreq):

    if tweet is None:
        tweet = ""

    words = tweet.encode('utf-8').split()
    #words = removeNone(tweet)
    score = 0
    for item in words:
        termfreq[item.lower()] = 0
    for item in words:
        if termfreq.get(item.lower()) is None:
            termfreq[item.lower()] = 0
        else:
            if(termfreq.has_key(item.lower())):
                termfreq[item.lower()] = termfreq[item.lower()] + 1
    return termfreq


def main():

    tweet_file = open(sys.argv[1])
    tweetsall = collectTweets(tweet_file)
    displayScore(tweetsall)

if __name__ == '__main__':
    main()
