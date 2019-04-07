import os
import word2vec
from scipy import spatial
import numpy as np
import re
import nltk

class Word2Vec():
    def __init__(self,
                 wiki_file_path = os.path.join("data","wiki_dk_clean_w2v.txt"),
                 w2v_binaries_path= os.path.join("embeddings","wiki_w2v.bin"),
                 overwrite=False):



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
                try:
                    vec = self.w2v[w]
                except:
                    raise Exception("I dont know", w)
                features.append(vec)

            result = np.average(features,axis=0)
            return result

        else:
            word = words[0].lower()
            try:
                vec = self.w2v[word]
            except:
                raise Exception("I dont know",word)
            return vec