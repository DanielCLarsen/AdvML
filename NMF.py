from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
import numpy as np
from scipy import spatial
import nltk.tokenize
import re
import nimfa
import sklearn.decomposition.nmf

class NMF():
    def __init__(self,bow,number_of_pc=100):
        self.vocab = bow.vocab
        #snmf = nimfa.Snmf(csr_matrix(bow(), dtype=float),seed="random_c", rank=number_of_pc, max_iter=1 , version='r', eta=1.,beta=1e-4, i_conv=10, w_min_change=0)
        #self.snmf_fit = snmf()
        tol = 1e-4
        print("stopping at: ",tol)
        nmf = sklearn.decomposition.nmf.NMF(n_components=number_of_pc,verbose=True,tol=tol)
        self.W = nmf.fit_transform(bow().transpose())

    def predict(self, words):
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
                features.append(self.W[word1_index,:])

            result = np.average(features,axis=0)
            return result

        else:
            word = words[0].lower()
            if not self.vocab.get(word):
                raise Exception("I dont know",word)
            word1_index = self.vocab.get(word)
            return self.W[word1_index,:]