import csv
import matplotlib.pyplot as plt
from Analyzer import Analyzer

data = []
total = 0

file_name = "results/LSA_2019-04-16 10:50:19.135723.csv"
file_unknown = "results/LSA_2019-04-16 10:50:19.135723_unknown.csv"

ana = Analyzer(file_name,file_unknown)

print(ana.get_acc())

name = "LSA"

plt.title("LSA Normalized")
plt.xlabel("Distance")
plt.ylabel("Count")
plt.hist(ana.get_norm_dist(),bins=50,color='blue',label='Normalized distances')
plt.legend(loc='upper right')
plt.savefig("images/"+name+"_normalized")
plt.show()

plt.title("LSA")
plt.xlabel("Distance")
plt.ylabel("Count")
plt.xlim(0,1)
plt.hist(ana.get_inlier_dist(),bins=50,alpha=0.5,color='green',label='Inlier distances')
plt.hist(ana.get_outlier_dist(),bins=50,alpha=0.5,color='red',label='Outlier distances')
plt.legend(loc='upper left')
plt.savefig("images/"+name)
plt.show()