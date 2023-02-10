import re

def profanity_score(tweet, profanity_words):
    # initialize a score variable
    score = 0
    # split the tweet into words
    words = tweet.split()
    # loop through each word in the tweet
    for word in words:
        # check if the word is in the profanity word list
        if word.lower() in profanity_words:
            # increase the score if the word is found
            score += 1
    # return the profanity score for the tweet
    return score
def profanity_analysis(filename, profanity_words):
    # open the file and read its contents
    with open(filename, 'r') as f:
        contents = f.read()
    # split the contents into tweets
    tweets = re.split(r'\n', contents)
    # initialize a list to store the profanity scores of each tweet
    scores = []
    # loop through each tweet
    for tweet in tweets:
        # calculate the profanity score of the tweet
        score = profanity_score(tweet, profanity_words)
        # add the score to the scores list
        scores.append(score)
    # return the scores list
    return scores
# list of profanity words
profanity_words = ['damn', 'hell', 'all', 'bitch', 'asshole', 'fuck']
# filename of the file containing the tweets
filename = 'tweets.txt'
# get the profanity scores for each tweet
scores = profanity_analysis(filename, profanity_words)
# print the scores
print(scores)
