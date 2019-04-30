import csv
import matplotlib.pyplot as plt
from Analyzer import Analyzer

data = []
total = 0

file_name = "results/OKAPI_2019-04-29 17:55:32.779216.csv"
file_unknown = "results/OKAPI_2019-04-29 17:55:32.779216_unknown.csv"

ana = Analyzer(file_name,file_unknown)

ana.get_outliers(1.5)
print("\n")
ana.get_outliers_below(1.01)

print("acc:",ana.get_acc(),"err:",ana.get_acc_error())

name = "OkapiBM25"
plt.rcParams.update({'font.size': 22,'figure.figsize': [10,10]})
plt.title("Okapi BM25 Normalized")
plt.xlabel("Distance ratio")
plt.ylabel("Count")
plt.hist(ana.get_norm_dist(),bins=50,color='blue',label='Normalized distances')
plt.legend(loc='upper right')
plt.savefig("images/"+name+"_normalized")
plt.show()


plt.title("Okapi BM25")
plt.xlabel("Distance")
plt.ylabel("Count")
plt.xlim(0,1)
plt.hist(ana.get_inlier_dist(),bins=50,alpha=0.5,color='green',label='Inlier distances')
plt.hist(ana.get_outlier_dist(),bins=50,alpha=0.5,color='red',label='Outlier distances')
plt.legend(loc='upper left')
plt.savefig("images/"+name)
plt.show()