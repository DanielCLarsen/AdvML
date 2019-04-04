from week1.BOW import BOW
from scipy.linalg import svd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

bow = BOW()
bow.load("texts.csv")




# SVD
U, s, VT = svd(bow.m)
print("size U:",U.shape)
print("size sigma:",s.shape)
print("size V.T:",VT.shape)

n_pc = 2
top = 4
for pc in range(n_pc):
    print("\n\nPC{}".format(pc))
    d = VT[pc, :].dot(s[pc])
    ind = np.argsort(np.abs(d))[-10:-1]
    for i in ind:
        for chap in bow.doc_index.keys():
            if bow.doc_index.get(chap) == i:
                print(chap,d[i])


n_pc = 2
top = 4
for pc in range(n_pc):
    print("\n\nPC{}".format(pc))
    t = U[:,pc].dot(s[pc])
    ind = np.argsort(np.abs(t))[-10:-1]
    for i in ind:
        for chap in bow.words_index.keys():
            if bow.words_index.get(chap) == i:
                print(chap,t[i])

print(s/np.sum(s))

