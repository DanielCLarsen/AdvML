import csv
from utils.odd_one_out_loader import load_odd_one_out
import os
import numpy as np

class Analyzer(object):
    def __init__(self,file_path,file_unknown_path,small=False):
        self.total = 0
        self.small = small
        self.__read_data(file_path,file_unknown_path)
        self.ooo = load_odd_one_out(os.path.join("data","odd_one_out_djt.csv"))

        if self.small:
            self.ooo = self.ooo[:100]
        print(self.total)
    def __read_data(self,file_path,file_unknown_path):
        f = open(file_path, 'r', encoding="utf8")
        fu = open(file_unknown_path, 'r', encoding="utf8")
        w = csv.reader(f)
        wu = csv.reader(fu)
        self.header = next(w)
        self.predictions = []
        self.distances = []
        self.indices = []
        self.data = []
        for row in w:
           self.total += 1
           if row:
               self.data.append(row)
               if len(row) > 2:
                   self.indices.extend([int(row[0])])
                   self.predictions.append(int(row[1][1]))
                   d = []
                   d.append(float(row[2]))
                   d.append(float(row[3]))
                   d.append(float(row[4]))
                   d.append(float(row[5]))
                   d.append(float(row[6]))
                   d.append(float(row[7]))
                   self.distances.append(d)
           if self.small and self.total>=100:
              break

    def get_predictions(self):
        return self.predictions

    def get_inlier_dist(self):
        inlier_dist = []
        for dis in self.distances:
            inlier_dist.extend(dis[:3])

        return inlier_dist

    def get_outlier_dist(self):
        outlier_dist = []
        for dis in self.distances:
            outlier_dist.extend(dis[3:])

        return outlier_dist


    def get_acc(self):
        print(self.total)
        return self.predictions.count(3)/self.total

    def get_norm_dist(self):
        norm_dist = []
        for dis in self.distances:
            outlier_dist = sum(dis[3:])
            inlier_dist = sum(dis[:3])
            norm_dist.append(outlier_dist/inlier_dist)

        return norm_dist

    def get_acc_error(self):
        acc = self.get_acc()
        err = np.sqrt( acc * (1 - acc) / self.total)
        return err

    def get_outliers(self,above):
        d = self.get_norm_dist()[0:100]
        while np.max(d) > above:


            print("distance ratio",np.max(d),self.ooo[np.argmax(d)],"prediction:",self.predictions[np.argmax(d)])

            d[np.argmax(d)] = 0

    def get_outliers_below(self, below):
        d = self.get_norm_dist()[0:100]
        while np.min(d) < below:
            print("distance ratio", np.min(d), self.ooo[np.argmin(d)],"prediction:",self.predictions[np.argmin(d)])

            d[np.argmin(d)] = 100

    def get_incorrect(self):
        incorrect = []
        for i,pred in enumerate(self.predictions):
            if pred != 3:
                incorrect.append(self.ooo[i])

        return incorrect

    def get_incorrect_indices(self):
        incorrect = set()
        for i,pred in enumerate(self.predictions):
            if pred != 3:
                incorrect.add(i)

        return incorrect

    def get_ooo(self,indices):
        odds = []
        for ind in indices:
            odds.append(self.ooo[ind])

        return odds

    def get_correct(self):
        correct = []
        for i, pred in enumerate(self.predictions):
            if pred == 3:
                correct.append(self.ooo[i])

        return correct

    def get_correct_indices(self):
        correct = set()
        for i, pred in enumerate(self.predictions):
            if pred == 3:
                correct.add(i)

        return correct

    def get_prediction(self,index):

        if len(self.data[index]) > 2:
            return int(self.data[index][1][1])
        else:
            return None

    def get_distance(self,index):

        if len(self.data[index]) > 2:
            d = []
            d.append(float(self.data[index][2]))
            d.append(float(self.data[index][3]))
            d.append(float(self.data[index][4]))
            d.append(float(self.data[index][5]))
            d.append(float(self.data[index][6]))
            d.append(float(self.data[index][7]))

            return d
        else:
            return None