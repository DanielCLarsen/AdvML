import csv
import matplotlib.pyplot as plt

data = []
total = 0

file_name = "results/OKAPI_2019-04-16 09:03:02.280620.csv"
file_unknown = "results/OKAPI_2019-04-16 09:03:02.280620_unknown.csv"

f = open(file_name,'r',encoding="utf8")
fu = open(file_unknown,'r',encoding="utf8")
w = csv.reader(f)
wu = csv.reader(fu)
header = next(w)
for row in w:
    total +=1
    if row:
        if len(row) > 2:
            d = [int(row[0])]
            d.append(int(row[1]))
            d.append(float(row[2]))
            d.append(float(row[3]))
            d.append(float(row[4]))
            d.append(float(row[5]))
            d.append(float(row[6]))
            d.append(float(row[7]))
            data.append(d)


predict = 0
inlier_dist = []
outlier_dist = []
for d in data:
    for i in range(2,5):
        inlier_dist.append(d[i])

    for i in range(5,8):
        outlier_dist.append(d[i])

    if d[1] == 3:
        predict+=1

print(predict/len(data))

plt.hist(inlier_dist,bins=50)
plt.hist(outlier_dist,bins=50)
plt.show()