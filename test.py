from nltk.book import *
from week1.BOW import BOW

bow = BOW()

d = {}

chapter_count = 1
for word in text1.tokens:

    if word == "chapter":
        bow.update_dict("chapter"+str(chapter_count), d)
        chapter_count +=1
        d = {}
    else:
        if d.get(word):
            d.update({word: d.get(word)+1})
        else:
            d.update({word:1})

bow.update_dict("chapter"+str(chapter_count+1),d)
bow.dump("texts.csv")