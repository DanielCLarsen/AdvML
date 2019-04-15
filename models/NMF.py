import numpy as np
import sklearn.decomposition.nmf
from model import Model
from scipy import spatial
import nltk.tokenize
import re

class NMF:
    def __init__(self,bow,number_of_pc=100):
        self.name = "NMF"
        self.vocab = bow.vocab
        tol = 1e-4
        print("stopping at: ",tol)
        nmf = sklearn.decomposition.nmf.NMF(n_components=number_of_pc,verbose=True,tol=tol)
        self.W = nmf.fit_transform(bow().transpose())

    def __get_feature(self,query):
        words = self.__split(query)
        feature = []

        for word in words:
            if not self.vocab.get(word):
                raise Exception("I dont know", word)
            word_index = self.vocab.get(word)

            feature.append(self.W[word_index,:])

        return np.average(feature, axis=0)

    def distance(self,word1,word2):
        v1 = self.__get_feature(word1)
        v2 = self.__get_feature(word2)

        return spatial.distance.cosine(v1, v2)

    def know(self, query):
        words = self.__split(query)

        for word in words:

            if not self.vocab.get(word):
                return False

        return True

    def __split(self, word):
        query = re.sub('[^A-Za-zøæå0-9]', ' ', word)
        words = nltk.tokenize.word_tokenize(query)
        words = [x.lower() for x in words]

        return words
