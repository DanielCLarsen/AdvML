import csv
import matplotlib.pyplot as plt
from Analyzer import Analyzer

data = []
total = 0

file_name = "results/LSA_2019-04-29 14:51:19.470121.csv"
file_unknown = "results/LSA_2019-04-29 14:51:19.470121_unknown.csv"

ana = Analyzer(file_name,file_unknown)

ana.get_outliers(10)
print("\n")
ana.get_outliers_below(0.9)

print("acc:",ana.get_acc(),"err:",ana.get_acc_error())

name = "LSA"

plt.rcParams.update({'font.size': 22,'figure.figsize': [10,10]})

plt.title("LSA Normalized")
plt.xlabel("Distance ratio")
plt.ylabel("Count")
plt.hist(ana.get_norm_dist(),bins=50,color='blue',label='Normalized distances')
plt.legend(loc='upper right')
plt.savefig("images/"+name+"_normalized")
plt.show()

plt.title("LSA Normalized")
plt.xlabel("Distance ratio")
plt.ylabel("Count")
plt.xlim(0,5)
plt.hist(ana.get_norm_dist(),bins=500,color='blue',label='Normalized distances')
plt.legend(loc='upper right')
plt.savefig("images/"+name+"_normalized_fitted")
plt.show()


#plt.title("LSA")
#plt.xlabel("Distance")
#plt.ylabel("Count")
#plt.xlim(0,1)
#plt.hist(ana.get_inlier_dist(),bins=50,alpha=0.5,color='green',label='Inlier distances')
#plt.hist(ana.get_outlier_dist(),bins=50,alpha=0.5,color='red',label='Outlier distances')
#plt.legend(loc='upper left')
#plt.savefig("images/"+name)
#plt.show()