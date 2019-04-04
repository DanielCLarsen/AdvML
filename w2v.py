import word2vec
from odd_one_out_loader import load_odd_one_out
import numpy as np

def classify_w2v_distance(words,model):
    dist = []
    for i in range(len(words)):
        #100 vector
        total_dist = 0
        for c in range(len(words)):
            if i != c:
                d = model.distance(words[i].lower(),words[c].lower())
                #print("dist:",d)
                total_dist += d[0][2]

        dist.append(total_dist)

    #print(dist)
    return np.argmin(dist)



model = word2vec.load('wikiw2v.bin')

odd_one_out = load_odd_one_out()

#q = 5

#index = classify_w2v_distance(odd_one_out[q],model)

#print(odd_one_out[q][index])

count = 0
correct = 0
dont_know = 0
for row in odd_one_out:
    try:
        index = classify_w2v_distance(row,model)
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