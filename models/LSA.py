from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
import numpy as np
from scipy import spatial
import nltk.tokenize
import re


class LSA:
    def __init__(self, bow, number_of_pc=100):
        # SVD
        U, s, VT = svds(csr_matrix(bow(), dtype=float), k=number_of_pc)
        self.vocab = bow.vocab
        self.sigma_k = np.diag(s[:number_of_pc])
        self.U_k = VT[ :number_of_pc,:]
        self.name = "LSA"
        print(self.name)
        print(self.U_k.shape)
        print(len(self.vocab))

    def __get_feature(self,query):
        words = self.__split(query)
        feature = []

        for word in words:
            if not self.vocab.get(word):
                raise Exception("I dont know", word)
            word_index = self.vocab.get(word)

            feature.append(self.U_k[:, word_index].dot(self.sigma_k))


        if not feature:
            raise Exception("empty feature")
        return np.average(feature, axis=0)

    def distance(self,word1,word2):
        print(word1,word2)
        v1 = self.__get_feature(word1)
        v2 = self.__get_feature(word2)
        print(type(v1))
        print(type(v2))
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

