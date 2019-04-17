from utils.odd_one_out_loader import load_odd_one_out
from utils.progress_bar import progress_bar
import os
import datetime
import csv
import numpy as np

class Evaluator:

    def __init__(self,model,dataset=os.path.join("data","odd_one_out_djt.csv")):

        file_name = self.__generate_name(model)

        file = open(os.path.join("results",file_name+".csv"),'w',encoding="utf8")
        file_unknown = open(os.path.join("results",file_name+"_unknown.csv"),'w',encoding="utf8")

        self.writer = csv.writer(file)
        self.writer_unknown = csv.writer(file_unknown)
        self.writer.writerow(["challenge","prediction","d12","d13","d23","d14","d24","d34"])
        odd_one_out = load_odd_one_out(dataset)

        self.__eval(model,odd_one_out)


    def __eval(self,model,odd_one_out):
        pb = progress_bar(len(odd_one_out))
        for i,row in enumerate(odd_one_out):
            if self.__know_words(row,model):

                distances = self.__distances(row,model)
                index = self.__predict(distances)
                data = [i,index]

                for d in distances:
                    data.append(d)

                self.writer.writerow(data)

            else:
                self.writer.writerow([i,"dont_know"])

            pb()


    def __know_words(self,row,model):
        #For each word in row, check if part of model.vocab, save unknown words.
        know = True
        for word in row:
            if not model.know(word):
                self.writer_unknown.writerow([word])
                know = False
        return know

    def __distances(self,words, model):
        distances = []
        for x in range(0,3):
            for y in range(x+1,3):
                distances.append(model.distance(words[x],words[y]))

        for x in range(0,3):
            distances.append(model.distance(words[x],words[3]))
        return distances

    def __predict(self, distances):

        one = distances[0] + distances[1] + distances[3]
        two = distances[0] + distances[2] + distances[4]
        three = distances[1] + distances[2] + distances[5]
        four = distances[3] + distances[4] + distances[5]

        return np.argmax([one,two,three,four])

    def __generate_name(self, model):
        current_time = datetime.datetime.utcnow()

        name = "{}_{}".format(model.name,current_time)

        return name





