from week1.BOW import BOW
from scipy.linalg import svd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

bow = BOW()
bow.load("texts.csv")


pca = PCA(n_components=4)

principalComponents = pca.fit_transform(bow.m)

print(principalComponents.shape)


for i in range(4):
    print("\n\nP{}".format(i))
    p = principalComponents[:,i]
    indeces = np.argsort(p)
    mind = indeces[-10:-1]
    for ind in mind:
        for k,v in bow.words_index.items():
            if v == ind:
                print(k,p[ind])
                break

for chap in bow.doc_index.keys():
    print(chap)
    p = principalComponents