import sys
import json
from collections import Counter

def main():

  hashtags = []

  # load each tweet as json
  for line in open(sys.argv[1]):
    tweet_json = json.loads(line)

    # if a tweet has a hashtag ...
    if "entities" in tweet_json.keys() and "hashtags" in tweet_json["entities"]:
      # and isn't blank ...
      if tweet_json['entities']['hashtags'] != []:
        # append each hashtag (in unicode)
        for hashtag in tweet_json["entities"]["hashtags"]:
          unicode_hashtag = hashtag["text"].encode('utf-8')
          hashtags.append(unicode_hashtag)

  # print top ten hashtag counts to stdout
  top_ten = Counter(hashtags).most_common(10)
  for key, value in top_ten:
    print key, float(value)

if __name__ == '__main__':
  main()