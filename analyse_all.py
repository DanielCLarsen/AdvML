import csv
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from Analyzer import Analyzer
import numpy as np
data = []
total = 0

file_name = "results/word2vec_2019-04-27 11:33:36.985787.csv"
file_unknown = "results/word2vec_2019-04-27 11:33:36.985787_unknown.csv"
ana_w2v = Analyzer(file_name,file_unknown)

file_name = "results/LSA_2019-04-27 11:39:58.283419.csv"
file_unknown = "results/LSA_2019-04-27 11:39:58.283419_unknown.csv"
ana_lsa = Analyzer(file_name,file_unknown)

file_name = "results/NMF_2019-04-28 14:54:07.830876.csv"
file_unknown = "results/NMF_2019-04-28 14:54:07.830876_unknown.csv"
ana_nmf = Analyzer(file_name,file_unknown)

file_name = "results/OKAPI_2019-04-28 16:02:33.394341.csv"
file_unknown = "results/OKAPI_2019-04-28 16:02:33.394341_unknown.csv"
ana_okapi = Analyzer(file_name,file_unknown)

word2vec = ana_w2v.get_incorrect_indices()
okapi = ana_okapi.get_incorrect_indices()
lsa = ana_lsa.get_incorrect_indices()
nmf = ana_nmf.get_incorrect_indices()

all = word2vec
all = all.intersection(okapi)
all = all.intersection(lsa)
all = all.intersection(nmf)
print(len(all))
print(ana_w2v.get_ooo(list(all)))

print(len(lsa))
print(len(nmf))

print(len(lsa.intersection(nmf)))
print(len(lsa.intersection(okapi)))
print(len(lsa.intersection(word2vec)))




v=venn3([lsa.intersection(nmf),word2vec,okapi], set_labels = ('LSA and NMF', 'Word2Vec', 'Okapi BM25'))
plt.show()
