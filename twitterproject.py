import json
from textblob  import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

tweetFile = open("tweetdata.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

text = []
polarity_list = []

for i in tweetData:
    text.append(i["text"])
    polarity_list.append(TextBlob(i["text"]).polarity)

giant_string_of_tweets = ""
for i in tweetData:
    giant_string_of_tweets += i["text"]

#word cloud
wordcloud = WordCloud(height = 1000, width = 1000).generate(giant_string_of_tweets)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('chart.png')

def wordcount(giant_string_of_tweets, string1):
    counter = 0
    string1 = string1.lower()
    wordlist = giant_string_of_tweets.split(' ')
    for item in wordlist:
        if item.lower() == string1:
            counter += 1
        return counter

wordcountlist =  []
for item in text:
    wordoccurences = wordcount(item, "the")
    wordcountlist.append(wordoccurences)

print(wordcountlist)
n, bins, patches = plt.hist(wordcountlist, 50)
plt.axis([min(wordcountlist), max(wordcountlist), 0, 50])
plt.grid(True)
plt.show()

def countletter(string, letter):
    counter = 0
    for let in string:
        if let.lower() == letter:
            counter += 1
        else: counter += 0
    return counter

countletter(giant_string_of_tweets, "a")
alpha = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
letters = sorted(alpha)

letteroccurences = []
for letter in letters:
    letteroccurences.append(countletter(giant_string_of_tweets, letter))

plt.hist(letteroccurences)
plt.axis([min(letteroccurences), max(letteroccurences), 0, 10])
plt.show()


favoriteCount = 0
numberOfFavoriteCounts = 0
for i in range(0,len(tweetData)):
    if "favorite_count" in tweetData[i]:
        favoriteCount += tweetData[i]['favorite_count']
        numberOfFavoriteCounts += 1

avg = favoriteCount / numberOfFavoriteCounts
print(avg)

tb = TextBlob("You are a brilliant computer scientist")
print(tb.polarity)

print("Tweet id: ", tweetData[0]["id"])
print("Tweet text: ", tweetData[0]["text"])

plt.hist(polarity_list)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.axis([-0.55, 1.10, 0, 50])
plt.grid(True)
plt.show()
