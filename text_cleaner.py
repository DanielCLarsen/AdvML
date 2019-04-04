import re
import nltk

def clean(text):
    text = re.sub('[^A-Za-zøæå]', ' ', text)
    text = text.lower()
    text_tokenized = nltk.word_tokenize(text)

    for word in text_tokenized:
        if word in nltk.corpus.stopwords.words('english'):
            text_tokenized.remove(word)

    return text_tokenized
