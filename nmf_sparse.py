import csv
import sys
import numpy as np
import scipy.sparse
from sklearn.feature_extraction.text import CountVectorizer
import nimfa
from odd_one_out_loader import load_odd_one_out

def load(filename):
    return scipy.sparse.load_npz(filename)

def classify_w2v_distance(words,dist_func):
    dist = []
    for i in range(len(words)):
        #100 vector
        total_dist = 0
        for c in range(len(words)):
            if i != c:
                d = dist_func.distance(words[i].lower(),words[c].lower())
                #print("dist:",d)
                total_dist += d[0][2]

        dist.append(total_dist)

    #print(dist)
    return np.argmin(dist)

b = load("SparseBOW.npz")
print(b.shape)


snmf = nimfa.Snmf(b, seed="random_vcol", rank=10, max_iter=5, version='l',
                  eta=1., beta=1e-4, i_conv=5, w_min_change=0)
snmf_fit = snmf()

print(snmf_fit.shape)

odd_one_out = load_odd_one_out()

count = 0
correct = 0
dont_know = 0
for row in odd_one_out:
    try:
        index = classify_w2v_distance(row)
        count+=1
        if index == 3:
            correct +=1
    except:
        print("dont know",row)
        dont_know+=1
        continue

print("acc",correct/count)
print("know",count)
print("dont_know",dont_know)
print("acc_with_dont_know",correct/(correct+dont_know))