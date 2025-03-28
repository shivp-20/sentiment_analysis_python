# Cleaning Text Steps
# 1) create a text file and take text from it
# 2) Convert the letter into lowercase
# 3) Remove the punctuations symbols
import string
from collections import Counter
import matplotlib.pyplot as plt

import GetOldTweets3 as got


def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus') \
        .setSince("2019-08-01") \
        .setUntil("2020-02-28") \
        .setMaxTweets(1000)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)[0]
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets


text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0] + " " + text
    # print(text)

# Text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = cleaned_text.split()
# print(tokenized_words)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# print(final_words)

# NLP Emotion Algorithm
# 1) check if the word on the final word list is also present in emotion.txt
# - open emotion file
# - Loop through each line and clear it
# - Extract the word and emotion using split

# 2) if word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(":")
        # print("Word:" + word + " " + "Emotion:" + emotion)

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
W = Counter(emotion_list)
print(W)

fig, axl = plt.subplots()
axl.bar(W.keys(), W.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
