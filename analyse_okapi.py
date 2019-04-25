import csv
import matplotlib.pyplot as plt
from Analyzer import Analyzer

data = []
total = 0

file_name = "results/OKAPI_2019-04-16 09:03:02.280620.csv"
file_unknown = "results/OKAPI_2019-04-16 09:03:02.280620_unknown.csv"

ana = Analyzer(file_name,file_unknown)

print(ana.get_acc())
print(ana.get_inlier_dist())
print(ana.get_outlier_dist())

name = "OkapiBM25"

plt.title("Okapi BM25 Normalized")
plt.xlabel("Distance")
plt.ylabel("Count")
plt.hist(ana.get_norm_dist(),bins=50,color='blue',label='Normalized distances')
plt.legend(loc='upper right')
plt.savefig("images/"+name+"_normalized")
plt.show()


plt.title("Okapi BM25")
plt.xlabel("Distance")
plt.ylabel("Count")
plt.xlim(0.5,1)
plt.hist(ana.get_inlier_dist(),bins=50,alpha=0.5,color='green',label='Inlier distances')
plt.hist(ana.get_outlier_dist(),bins=50,alpha=0.5,color='red',label='Outlier distances')
plt.legend(loc='upper left')
plt.savefig("images/"+name)
plt.show()