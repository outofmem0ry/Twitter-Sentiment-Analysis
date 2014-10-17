import sys
import json
from collections import defaultdict

# Function to create dictionary of words and their scores from AFINN-111.txt
def createSentimentDictionary(afinnfile):
    scores = {}  # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores


# Function to collect tweets from the text file.
def collectTweetsandLocation(f):
    data = []
    for line in f:
        data.append(json.loads(line, encoding='UTF-8'))
    tweets = []
    location = []
    count = 0
    while (count < len(data)):
        if (data[count].has_key("user"))&(data[count].has_key('text')):
            tweets.append(data[count].get('text'))
            location.append(data[count]['user']['location'])
        count = count + 1
    return tweets,location


# def collectLocation(f):
#     data = []
#     for line in f:
#         data.append(json.loads(line, encoding='UTF-8'))
#     location = []
#     countl = 0
#     while (countl < len(data)):
#         if (data[countl].has_key("user")):
#             location.append(data[countl]['user']['location'])
#         countl = countl + 1
#     return location


# Function to store the scores into a list or dictionary or tuples.
# Argument 'tweets'

def displayScore(tweetsall, sentimentscores):
    locdict = defaultdict(dict)
    # loclist = []
    # locdict = {'',0}
    for tweetnumber in range(len(tweetsall[0])):
        tweetscore = calculateSentimentScore(tweetsall[0][tweetnumber], sentimentscores)
        loc = {tweetsall[1][tweetnumber].encode('utf-8'):tweetscore}
        locdict.update(loc)
        #locdict = {tweetsall[1][tweetnumber]:tweetscore}

        tweetnumber = tweetnumber + 1
        #print tweetscore
        #locdict.update(tweetsall[1][tweetnumber],tweetscore)
        # locdict.update(loclist)
    return locdict
# Calculate score function which need a tweet s an input so that it can compute the score.

def calculateSentimentScore(tweet, scores):
    if tweet is None:
        tweet = ""
    words = tweet.encode('utf-8').split(" ")
    #locations = location.encode('utf-8').split(" ")
    # words = removeNone(tweet)
    score = 0
    for item in words:
        if scores.has_key(item.lower()):
            score = score + scores[item.lower()]
        else:
            score = score
    return score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    d={}
    sentimentscores = createSentimentDictionary(sent_file)
    tweetsall = collectTweetsandLocation(tweet_file)
    d = displayScore(tweetsall, sentimentscores)
    sp = str(d.keys())
    allkeys = sp.split()
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    k={}
    for key in allkeys:
        if key in states.iterkeys():
            k[key] = 0
    for val in k.keys():
        k[key] = (d.get(val))

    max = 0
    s=[]
    state = ''
    vals = k.values()
    for i in range(len(vals)):
        if vals[i] > max:
         max = vals[i]
    max=int(max)
    for newval in k.keys():
        if k.get(newval)==max:
            state = newval
    #rint state.strip()
    #print(state, end="", flush=True)
    sys.stdout.write(state)


if __name__ == '__main__':
    main()
