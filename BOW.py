import numpy as np
import nltk
from text_cleaner import clean
import csv
import json
from scipy.sparse.dok import dok_matrix
from progress_bar import progress_bar
import gc

class BOW(object):

    def __init__(self,language):
        self.language = language
        self.bow = {}
        self.words = set()
        self.total = {}

    def update_dict(self,doc_name : str, word_dict : dict):
        self.bow.update({doc_name:word_dict})
        self.words.update(word_dict.keys())
        for word in word_dict.keys():
            if self.total.get(word):
                self.total.update({word:word_dict.get(word)+self.total.get(word)})
            else:
                self.total.update({word:word_dict.get(word)})

    def update_text(self,doc_name : str, text : str):

        tokenized_text = clean(text)
        word_dict = nltk.Counter(tokenized_text)

        self.bow.update({doc_name:word_dict})
        self.words.update(word_dict.keys())

        for word in word_dict.keys():
            if self.total.get(word):
                self.total.update({word:word_dict.get(word)+self.total.get(word)})
            else:
                self.total.update({word:word_dict.get(word)})

    def update_text_fast(self,doc_name : str, text : str):

        text_tokenized = nltk.word_tokenize(text)

        text_tokenized = self._remove_stopwords(text_tokenized)

        word_dict = nltk.Counter(text_tokenized)

        self.bow.update({doc_name:word_dict})
        self.words.update(word_dict.keys())

        for word in word_dict.keys():
            if self.total.get(word):
                self.total.update({word:word_dict.get(word)+self.total.get(word)})
            else:
                self.total.update({word:word_dict.get(word)})

    def _remove_stopwords(self,token_text):
        words_to_delete = set(nltk.corpus.stopwords.words(self.language)).intersection(set(token_text))
        for w in words_to_delete:
            token_text.remove(w)

        return token_text

    def exlude(self,occ):

        words_to_delete = set()

        pb = progress_bar(len(self.total.keys()),title="finding words to delete")
        for word,tot in self.total.items():
            pb()

            if occ > tot:
                words_to_delete.add(word)

        pb = progress_bar(len(self.bow.keys()),title="deleting those words from documents")
        for doc in self.bow.keys():
            pb()
            dw = set(self.bow.get(doc).keys()).intersection(words_to_delete)
            for word in dw:
                self.bow.get(doc).pop(word)

        self.words.difference_update(words_to_delete)
    def as_numpy(self):
        number_of_docs = len(self.bow.keys())
        number_of_words = len(self.words)

        self.words_index = {}
        for i,word in enumerate(self.words):
            self.words_index.update({word:i})

        self.doc_index = {}
        for i,doc_name in enumerate(self.bow.keys()):
            self.doc_index.update({doc_name:i})

        print(number_of_words)
        print(number_of_docs)

        self.m = np.zeros((number_of_words,number_of_docs))

        print(self.m.shape)
        pb = progress_bar(number_of_docs,title="converting to numpy")
        for doc , word_dict in self.bow.items():
            pb()

            for word in word_dict.keys():
                self.m[ self.words_index.get(word) , self.doc_index.get(doc) ] = word_dict.get(word)/self.total.get(word)

        #self._normalize()

        return self.m

    def dump(self,filename):
        self.as_numpy()
        pb = progress_bar(self.m.shape[0],title="writing bow to file")
        with open(filename,'w') as f:
            w = csv.writer(f)
            w.writerow(json.dumps(self.doc_index))
            w.writerow(json.dumps(self.words_index))
            for entry in range(self.m.shape[0]):
                w.writerow(self.m[entry,:])
                pb()

    def _normalize(self):
        pb = progress_bar(len(self.words_index.keys()),title="normalizing bow")
        for w,i in self.words_index.items():
            pb()
            self.m[i,:] /= self.total.get(w)

    def load(self,file_name):
        with open(file_name,'r') as f:
            r = csv.reader(f)
            docs = next(r)

            t = ""
            for d in docs:
                t += d
            self.doc_index = json.loads(t)


            words = next(r)

            t = ""
            for w in words:
                t += w
            self.words_index = json.loads(t)


            number_of_docs = len(self.doc_index)
            number_of_words = len(self.words_index)

            print(number_of_words)
            print(number_of_docs)

            self.m = np.zeros((number_of_words,number_of_docs))

            print(self.m.shape)
            count = 0
            for row in r:
                self.m[count,:] = row
                count +=1


class BOW_sparse(BOW):

    def as_numpy(self):
        number_of_docs = len(self.bow.keys())
        number_of_words = len(self.words)

        self.words_index = {}
        for i,word in enumerate(self.words):
            self.words_index.update({word:i})

        self.doc_index = {}
        for i,doc_name in enumerate(self.bow.keys()):
            self.doc_index.update({doc_name:i})

        print(number_of_words)
        print(number_of_docs)

        self.words = None
        gc.collect()

        self.m = dok_matrix((number_of_words,number_of_docs))

        print(self.m.shape)
        pb = progress_bar(number_of_docs,title="converting to numpy")
        for doc , word_dict in self.bow.items():
            pb()
            for word in word_dict.keys():
                self.m[ self.words_index.get(word) , self.doc_index.get(doc) ] = word_dict.get(word)/self.total.get(word)

        #self._normalize()

        return self.m

    def dump(self,filename):
        self.as_numpy()
        pb = progress_bar(self.m.shape[0],title="writing bow to file")
        with open(filename,'w') as f:
            w = csv.writer(f)
            w.writerow(json.dumps(self.doc_index))
            w.writerow(json.dumps(self.words_index))
            for entry in range(self.m.shape[0]):
                w.writerow(self.m[entry,:])
                pb()

    def load(self,file_name):
        with open(file_name,'r') as f:
            r = csv.reader(f)
            docs = next(r)

            t = ""
            for d in docs:
                t += d
            self.doc_index = json.loads(t)


            words = next(r)

            t = ""
            for w in words:
                t += w
            self.words_index = json.loads(t)


            number_of_docs = len(self.doc_index)
            number_of_words = len(self.words_index)

            print(number_of_words)
            print(number_of_docs)

            self.m = dok_matrix((number_of_words,number_of_docs))

            print(self.m.shape)
            count = 0
            for row in r:
                self.m[count,:] = row
                count +=1