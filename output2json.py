import json

# Function to create dictionary of words and their scores from AFINN-111.txt

afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

# print scores.items() # Print every (term, score) pair in the dictionary

# Function to collect tweets from the text file.
data  = [ ]
with open('output.txt') as f:
    for line in f:
        data.append(json.loads(line,encoding = 'UTF-8'))

tweets = [ ]
count = 0
while (count < len(data)):
   tweets.append(data[count].get('text'))
   count = count + 1


location = [ ]
countl = 0
while (countl < len(data)):
    if(data[countl].has_key("user")):
        location.append(data[countl]['user']['location'])
    countl = countl + 1
print location
# Calculate score function which need a tweet s an input so that it can compute the score.

words = tweets[13].encode('utf-8').split(" ")
print words
score = 0 
for item in words:
    if scores.has_key(item.lower()):
       score = score + scores[item.lower()]
    else:
      score = score + 0



##  # Need a fucntion to store the scores into a list or dictionary or tuples.
##  # Argument 'tweets'
##
##  tweetnumber = 0
##   for tweetnumber in range(len(tweets)):
##     tweetscore = calculatescore(tweets[tweetnumber]))
##     print tweetscore
   
   
   
