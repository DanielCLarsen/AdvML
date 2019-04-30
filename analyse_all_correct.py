import csv
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from Analyzer import Analyzer
import numpy as np
data = []
total = 0

file_name = "results/word2vec_2019-04-29 14:41:10.729714.csv"
file_unknown = "results/word2vec_2019-04-29 14:41:10.729714_unknown.csv"
ana_w2v = Analyzer(file_name,file_unknown)

file_name = "results/LSA_2019-04-29 14:51:19.470121.csv"
file_unknown = "results/LSA_2019-04-29 14:51:19.470121_unknown.csv"
ana_lsa = Analyzer(file_name,file_unknown)

file_name = "results/NMF_2019-04-29 17:55:18.441480.csv"
file_unknown = "results/NMF_2019-04-29 17:55:18.441480_unknown.csv"
ana_nmf = Analyzer(file_name,file_unknown)

file_name = "results/OKAPI_2019-04-29 17:55:32.779216.csv"
file_unknown = "results/OKAPI_2019-04-29 17:55:32.779216_unknown.csv"
ana_okapi = Analyzer(file_name,file_unknown)

word2vec = ana_w2v.get_correct_indices()
okapi = ana_okapi.get_correct_indices()
lsa = ana_lsa.get_correct_indices()
nmf = ana_nmf.get_correct_indices()

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

nmf_correct = nmf.difference(okapi)
nmf_correct = nmf_correct.difference(word2vec)
for index in nmf_correct:
    print("nmf_correct",ana_nmf.ooo[index])

print(len(nmf_correct))

v=venn3([lsa.union(nmf),word2vec,okapi], set_labels = ('LSA and NMF', 'Word2Vec', 'Okapi BM25'),)
plt.show()



