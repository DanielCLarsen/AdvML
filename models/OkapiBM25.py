import numpy as np
from scipy import spatial
import nltk.tokenize
import re

class OkapiBM25:
    def __init__(self,bow):
        self.bow = bow
        self.vocab=bow.vocab
        self.name="OKAPI"

    def __get_feature(self,query):
        words = self.__split(query)
        feature = []

        for word in words:
            if not self.vocab.get(word):
                raise Exception("I dont know", word)
            feature.append(self.___get_score(word))

        return np.sum(feature, axis=0)


    def ___get_score(self,word):
        i = self.vocab.get(word)
        N = self.bow().shape[0]
        #print(self.bow().shape)
        non_zero = self.bow()[:, i].count_nonzero()
        IDF = np.log((N - non_zero + 0.5) / non_zero + 0.5)
        freq_doc = self.bow()[:, i]
        doc_leng = self.bow().sum(axis=1)
        avg_doc = doc_leng.sum() / N

        #print(type(avg_doc))
        #print("doc_leng",doc_leng.shape)
        #print("freq_doc",freq_doc.shape)


        #k1 = [1.2, 2]
        k1 = 1.2
        b = 0.75

        upper = (freq_doc*(k1+1))
        c = k1*(1-b+b*(doc_leng/avg_doc))
        #print(c.shape)

        #print(non_zero)
        nn = freq_doc.nonzero()
        for i in range(non_zero):
            doc_i =nn[0][i]
            term_i = nn[1][i]
            freq_doc[doc_i,0]+=k1*(1-b+b*(doc_leng[doc_i,0]/avg_doc))
            upper[doc_i,0] /= freq_doc[doc_i,0]

        score = IDF * upper
        #print(score.shape)
        #print(score)
        return score

    def distance(self,word1,word2):

        v1 = self.__get_feature(word1)
        v2 = self.__get_feature(word2)

        return spatial.distance.cosine(v1.todense(), v2.todense())

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
