from textblob import TextBlob

wiki = TextBlob("Andrew is a cool dude")

print(wiki.tags)
print(wiki.words)
print(wiki.sentiment.polarity)