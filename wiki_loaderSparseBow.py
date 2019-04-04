import csv
import sys
import numpy as np
import scipy.sparse
from sklearn.feature_extraction.text import CountVectorizer
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

def dump(sparse_matrix,filename):
    scipy.sparse.save_npz(filename, sparse_matrix)

def load(filename):
    return scipy.sparse.load_npz(filename)



f = open("wiki_dk_clean.csv",'r',encoding="utf8")
r = csv.reader(f)
vectorizer = CountVectorizer()
data_corpus = []
for row in r:
    if row:
        data_corpus.append(row[1])

X = vectorizer.fit_transform(data_corpus)
dump(X,"SparseBOW")


