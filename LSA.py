from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
import numpy as np
from scipy import spatial
import nltk.tokenize
import re

class LSA():
    def __init__(self,bow,number_of_pc=100):
        # SVD
        U, s, VT = svds(csr_matrix(bow(), dtype=float), k=number_of_pc)
        self.vocab = bow.vocab
        self.sigma_k = np.diag(s[:number_of_pc])
        self.U_k = VT[ :number_of_pc,:]
        print(self.U_k.shape)
        print(len(self.vocab))
    def predict(self,words):
        dist = []
        for i in range(len(words)):
            total_dist = 0
            v1 = self.__get_feature(words[i])
            for c in range(len(words)):
                if i != c:
                    v2 = self.__get_feature(words[c])
                    d = 1 - spatial.distance.cosine(v1, v2)

                    # print("dist:",d)
                    total_dist += d

            dist.append(total_dist)

        # print(dist)
        return np.argmin(dist)

    def __get_feature(self,query):
        query = re.sub('[^A-Za-zøæå0-9]', ' ', query)
        words = nltk.tokenize.word_tokenize(query)

        if len(words) > 1:
            features = []
            for word in words:
                w = word.lower()
                if not self.vocab.get(w):
                    raise Exception("I dont know", w)
                word1_index = self.vocab.get(w)
                features.append(self.U_k[:, word1_index].dot(self.sigma_k))

            result = np.average(features,axis=0)
            return result

        else:
            word = words[0].lower()
            if not self.vocab.get(word):
                raise Exception("I dont know",word)
            word1_index = self.vocab.get(word)
            return self.U_k[:, word1_index].dot(self.sigma_k)