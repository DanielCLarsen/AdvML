import csv
import matplotlib.pyplot as plt
from Analyzer import Analyzer

data = []
total = 0

file_name = "results/NMF_2019-04-16 15:06:19.412936.csv"
file_unknown = "results/NMF_2019-04-16 15:06:19.412936_unknown.csv"

ana = Analyzer(file_name,file_unknown)

print(ana.get_acc())

name = "NMF"

plt.title("NMF Normalized")
plt.xlabel("Distance")
plt.ylabel("Count")
plt.hist(ana.get_norm_dist(),bins=50,color='blue',label='Normalized distances')
plt.legend(loc='upper right')
plt.savefig("images/"+name+"_normalized")
plt.show()




plt.title("NMF")
plt.xlabel("Distance")
plt.ylabel("Count")
plt.xlim(0,1)
plt.hist(ana.get_inlier_dist(),bins=50,alpha=0.5,color='green',label='Inlier distances')
plt.hist(ana.get_outlier_dist(),bins=50,alpha=0.5,color='red',label='Outlier distances')
plt.legend(loc='upper left')
plt.savefig("images/"+name)
plt.show()