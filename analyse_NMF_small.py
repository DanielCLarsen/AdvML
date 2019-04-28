import csv
import matplotlib.pyplot as plt
from Analyzer import Analyzer
import numpy as np

data = []
total = 0

file_name = "results/NMF_2019-04-28 14:54:07.830876.csv"
file_unknown = "results/NMF_2019-04-28 14:54:07.830876_unknown.csv"

ana = Analyzer(file_name,file_unknown,small=True)

ana.get_outliers(10)
print("\n")
ana.get_outliers_below(0.4)

print("acc:",ana.get_acc(),"err:",ana.get_acc_error())

name = "NMF"
plt.rcParams.update({'font.size': 22,'figure.figsize': [10,10]})
plt.title("NMF Normalized small")
plt.xlabel("Distance ratio")
plt.ylabel("Count")
plt.hist(ana.get_norm_dist(),bins=50,color='blue',label='Normalized distances')
plt.legend(loc='upper right')
plt.savefig("images/"+name+"_normalized_small")
plt.show()


plt.title("NMF Normalized small")
plt.xlabel("Distance ratio")
plt.ylabel("Count")
plt.xlim(0,5)
plt.hist(ana.get_norm_dist(),bins=500,color='blue',label='Normalized distances')
plt.legend(loc='upper right')
plt.savefig("images/"+name+"_normalized_fitted_small")
plt.show()


plt.title("NMF small")
plt.xlabel("Distance")
plt.ylabel("Count")
plt.xlim(0,1)
plt.hist(ana.get_inlier_dist(),bins=50,alpha=0.5,color='green',label='Inlier distances')
plt.hist(ana.get_outlier_dist(),bins=50,alpha=0.5,color='red',label='Outlier distances')
plt.legend(loc='upper left')
plt.savefig("images/"+name+"_small")
plt.show()