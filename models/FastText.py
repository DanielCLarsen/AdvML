import os
import word2vec
import numpy as np
from scipy import spatial
import nltk.tokenize
import re
import fasttext
class FastText:
    def __init__(self,
                 wiki_file_path = os.path.join("data","wiki_dk_clean_w2v.txt"),
                 ft_binaries_path= os.path.join("embeddings","wiki_w2v.bin")):

        self.name = "FastText"
        self.ft = fasttext.load_model(ft_binaries_path)

    def __call__(self, word):
        return self.ft[word]

    def __get_feature(self,query):

        words = self.__split(query)
        feature = []

        for word in words:
            try:
                vec = self.ft[word]
            except:
                raise Exception("I dont know", word)

            feature.append(vec)

        return np.average(feature, axis=0)

    def know(self,query):
        words = self.__split(query)

        for word in words:
            try:
                self.ft[word]
            except:
                return False
        return True

    def distance(self,word1,word2):
        v1 = self.__get_feature(word1)
        v2 = self.__get_feature(word2)

        return spatial.distance.cosine(v1, v2)

    def __split(self, word):
        query = re.sub('[^A-Za-zøæå0-9]', ' ', word)
        words = nltk.tokenize.word_tokenize(query)
        words = [x.lower() for x in words]

        return words
