import csv
import sys
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def dump(filename):
    with open(filename, 'w') as f:
        w = csv.writer(f)
        w.writerow(json.dumps(self.doc_index))
        w.writerow(json.dumps(self.words_index))
        for entry in range(self.m.shape[0]):
            w.writerow(self.m[entry, :])

f = open("wiki_dk_clean_small.csv",'r')
r = csv.reader(f)
vectorizer = CountVectorizer()
data_corpus = []
for row in r:
    if row:
        data_corpus.append(row[1])



X = vectorizer.fit_transform(data_corpus)
XM = X.toarray()
XM = np.transpose(XM)
print(vectorizer.get_feature_names())

