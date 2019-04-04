from BOW import BOW
from scipy.linalg import svd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from odd_one_out_loader import load_odd_one_out

def classify_euclidian_distance(words):
    dist = []
    for i in range(len(words)):
        #100 vector
        total_dist = 0
        for c in range(len(words)):
            if i != c:
                print("dist:",np.abs(np.linalg.norm(words[i] - words[c])))
                total_dist += np.linalg.norm(words[i] - words[c])

        dist.append(total_dist)

    print(dist)
    return np.argmax(dist)


bow = BOW("danish")
bow.load("bow_wiki_clean_small.csv")

print(bow.m.shape)

# SVD
U, s, VT = svd(bow.m)
print("size U:",U.shape)
print("size sigma:",s.shape)
print("size V.T:",VT.shape)

number_of_pc = 100


sigma_k = np.diag(s[:number_of_pc])
print("sigma_k:",sigma_k.shape)


U_k = U[:,:number_of_pc]
print("U_k",U_k.shape)


print("sigma_k -1",np.linalg.inv(sigma_k))
odd_one_out = load_odd_one_out()

count = 0
correct = 0
dont_know = 0
for row in odd_one_out:
    try:
        index = classify_euclidian_distance(row)
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