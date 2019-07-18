# In this program, we print out all the text data from our twitter JSON file.
# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format

import json
from textblob  import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.

tweetFile = open("tweetdata.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# We use the JSON library to get data from the file as JSON data.
text = []
polarity_list = []

for i in range(0,len(tweetData)):
    text.append(tweetData[i]["text"])
    polarity_list.append(TextBlob(tweetData[i]["text"]).polarity)

# print(len(polarity_list),lent(text))
giant_string_of_tweets = ""
for i in range(0,len(tweetData)):
    giant_string_of_tweets = tweetData[i]["text"]

# plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
# plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
# plt legend()

# print(type(tweetData))
# print(type(tweetData[0]))

# print(type(tweetData[0].keys()))

# print(tweetData[0]["favorite_count"])

# We can close the file now that we have locally stored the data.
# print(list(tweetData[0].keys()))

text = "Hello, it's me Maeghan!"
wordcloud = WordCloud().generate(giant_string_of_tweets)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('chart.png')

tweetlist = ""
tweetstring = ""
for tweet in tweetlist:
    tweet = tweet + ""
    tweetstring += tweet
print(tweetstring)

favoriteCount = 0
numberOfFavoriteCounts = 0

for i in range(0,len(tweetData)):

    if "favorite_count" in tweetData[i]:
        favoriteCount += tweetData[i]['favorite_count']
        numberOfFavoriteCounts += 1

avg = favoriteCount / numberOfFavoriteCounts
# print(avg)
#
# print(len(tweetData))
#
tweet = []
for i in range(len(tweetData)):
    tempTweet =  tweetData[i]["text"]
    tweet.append(tempTweet)

# print(tweet)
# tb = TextBlob("You are a brilliant computer scientist")
# print(tb.polarity)

PolarityList =[]
for i in range(0, len(tweet)):
    blob1 = TextBlob(tweet[i])
    polar1 = blob1.polarity
    PolarityList.append(polar1)

# for tweet in tweetData:
#     if "text" in tweet:
#         text = tweet["text"]
#         for index in range(26):
#         print(index)
#         nums[index] += numOfLetter(text, alpha[index])
# tweetData[0]["text"]

# We then print the data of ONE tweet:
# the [0] denotes the *first* tweet object.
# We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])

# First ask students how they might print the text object:
# Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])

# We're using index and counting the number of tweets in the tweetData
# using the python len() function.
# for idx in range(len(tweetData)):
# print("Tweet text: " + tweetData[idx]["text"])

# Explain here how Python lets you get objects
# directly without having to use an index.
# for tweet in tweetData:
# print("Tweet text: " + tweet["text"])
