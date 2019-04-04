import csv
import sys
import numpy as np
import scipy.sparse
from sklearn.feature_extraction.text import CountVectorizer

def dump(sparse_matrix,filename):
    scipy.sparse.save_npz(filename, sparse_matrix)

def load(filename):
    return scipy.sparse.load_npz(filename)



f = open("wiki_dk_clean_small.csv",'r')
r = csv.reader(f)
vectorizer = CountVectorizer()
data_corpus = []
for row in r:
    if row:
        data_corpus.append(row[1])

X = vectorizer.fit_transform(data_corpus)
dump(X,"SparseBOW")


