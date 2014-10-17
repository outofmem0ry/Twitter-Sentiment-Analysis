import sys
import json

def build_sent_dict(sentfile):
    scores = {} # initialize an empty dictionary
    for line in sentfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = build_sent_dict(sent_file)

    derived_sent_score = {}
    word_freq = {}
    
    for line in tweet_file:
        
        tweet = json.loads(line)
        if "text" in tweet:
            tweet_sent_score = 0.0
            tweet = tweet["text"].encode('utf-8').split()
            for word in tweet:
                if word in sent_scores:
                    tweet_sent_score += sent_scores[word]
                
            for word in tweet:
                if word not in sent_scores:
                    if word not in derived_sent_score:
                        derived_sent_score[word] = tweet_sent_score
                        word_freq[word] = 1
                    else:
                        derived_sent_score[word] += tweet_sent_score
                        word_freq[word] += 1
                    
    for word in derived_sent_score:
        derived_sent_score[word] /= word_freq[word]
        print word, str(derived_sent_score[word])

if __name__ == '__main__':
    main()