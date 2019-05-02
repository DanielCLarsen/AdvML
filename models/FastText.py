import os
import word2vec
import numpy as np
from scipy import spatial
import nltk.tokenize
import re
import fastText

class FastText:
    def __init__(self,
                 wiki_file_path = os.path.join("data","wiki_dk_clean_w2v.txt"),
                 ft_binaries_path= os.path.join("embeddings","wiki_w2v.bin"),train=False):

        self.name = "FastText"

        if train:
            self.ft = fastText.FastText.train_unsupervised("data/wiki_dk_clean_w2v.txt", dim=100)
            self.ft.save_model("embeddings/ft.bin")
        else:
            self.ft = fastText.load_model(ft_binaries_path)


    def __call__(self, word):
        return self.ft[word]

    def __get_feature(self,query):

        words = self.__split(query)
        feature = []

        for word in words:
            try:
                vec = self.ft.get_word_vector(word)
            except:
                raise Exception("I dont know", word)

            feature.append(vec)

        return np.average(feature, axis=0)

    def know(self,query):
        words = self.__split(query)
        for word in words:
            try:

                if self.ft.get_word_id(word) == -1:
                    print("dont know",word," ",self.ft.get_subwords(word))

                self.ft.get_word_vector(word)
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
