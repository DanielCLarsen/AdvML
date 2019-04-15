import os
import word2vec
import numpy as np
from scipy import spatial
import nltk.tokenize
import re

class Word2Vec:
    def __init__(self,
                 wiki_file_path = os.path.join("data","wiki_dk_clean_w2v.txt"),
                 w2v_binaries_path= os.path.join("embeddings","wiki_w2v.bin"),
                 overwrite=False):

        self.name = "word2vec"


        if os.path.isfile(w2v_binaries_path) and not overwrite:
            print("loading w2v from: ",w2v_binaries_path)
            self.w2v = word2vec.load(w2v_binaries_path)
        else:
            print("w2v not found at: ",w2v_binaries_path)
            print("Creating w2v first")

            word2vec.word2vec(wiki_file_path, w2v_binaries_path, size=100, verbose=True)

            print("loading w2v from: ", w2v_binaries_path)
            self.w2v = word2vec.load(w2v_binaries_path)

    def __call__(self, word):
        return self.w2v[word]

    def __get_feature(self,query):

        words = self.__split(query)
        feature = []

        for word in words:
            try:
                vec = self.w2v[word]
            except:
                raise Exception("I dont know", word)

            feature.append(vec)

        return np.average(feature, axis=0)

    def know(self,query):
        words = self.__split(query)

        for word in words:
            try:
                self.w2v[word]
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
