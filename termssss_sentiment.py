import sys
import json
from collections import defaultdict
# Function to create dictionary of words and their scores from AFINN-111.txt
def createSentimentDictionary(afinnfile):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores
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

def displayScore(tweetsall,sentimentscores):
    tweetnumber = 0
    tweetscore = defaultdict(list)
    termscore = {'':(0,0)}
    # termcount = {'':0}
    for tweetnumber in range(len(tweetsall)):
        tweetscore.update(calculateSentimentScore(tweetsall[tweetnumber],sentimentscores,termscore))
        tweetnumber = tweetnumber +1
    # print tweetscore
    tweetscore.pop('')
    words = tweetscore.keys()
    for w in words:
        avg = tweetscore[w][0]/tweetscore[w][1]
        print w,float(avg)


# Calculate score function which need a tweet s an input so that it can compute the score.

def calculateSentimentScore(tweet, scores,termscore):

    if tweet is None:
        tweet = ""

    words = tweet.encode('utf-8').split(" ")
    #words = removeNone(tweet)
    score = 0
    termavg = []
    for item in words:
        if scores.has_key(item.lower()):
            score = score + scores[item.lower()]
        else:
            score = score + 0
            termscore[item.lower()] = (0,0)
    for item in words:
        if scores.has_key(item.lower()) == False:
            if termscore.get(item.lower()) is None:
                termscore[item.lower()] = (termscore[''][0]+score,termscore[''][1]+0)
            else:
                if(termscore.has_key(item.lower())):
                    termscore[item.lower()] = (termscore[item.lower()][0]+score,termscore[item.lower()][1]+1)
    return termscore


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentimentscores =  createSentimentDictionary(sent_file)
    tweetsall = collectTweets(tweet_file)
    displayScore(tweetsall,sentimentscores)

if __name__ == '__main__':
    main()
