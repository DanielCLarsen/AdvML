import numpy as np
from scipy import spatial
class OkapiBM25():
    def __init__(self,bow):
        self.bow = bow
        self.vocab=bow.vocab

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

    def __get_feature(self,words):
        if type(words) == list:
            sum=None
            for word in words:
                if sum:
                    sum += self.___get_score(word)
                else:
                    sum = self.___get_score(word)
        else:
            return self.___get_score(words)


    def ___get_score(self,word):
        i = self.vocab.get(word)
        N = self.bow().shape[0]
        non_zero = self.bow()[:, i].count_nonzero()
        IDF = np.log((N - non_zero + 0.5) / non_zero + 0.5)
        freq_doc = self.bow()[:, i]
        doc_leng = self.bow().sum(axis=0)
        avg_doc = doc_leng.sum() / N

        print(type(avg_doc))
        print(doc_leng.shape)


        #k1 = [1.2, 2]
        k1 = 1.2
        b = 0.75

        tes = freq_doc+k1
        print(tes.shape)

        upper = (freq_doc*(k1+1))
        lower = (freq_doc+k1*(1-b+b*(doc_leng/avg_doc)))
        score = IDF* (upper/lower)
        print(score.shape)
        return score