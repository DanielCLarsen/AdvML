from Analyzer import Analyzer
import numpy as np

class Ensemble(object):
    def __init__(self,small=False):
        file_name = "results/word2vec_2019-04-29 14:41:10.729714.csv"
        file_unknown = "results/word2vec_2019-04-29 14:41:10.729714_unknown.csv"
        self.ana_w2v = Analyzer(file_name, file_unknown,small=small)

        file_name = "results/LSA_2019-04-29 14:51:19.470121.csv"
        file_unknown = "results/LSA_2019-04-29 14:51:19.470121_unknown.csv"
        self.ana_lsa = Analyzer(file_name, file_unknown,small=small)

        file_name = "results/NMF_2019-04-29 17:55:18.441480.csv"
        file_unknown = "results/NMF_2019-04-29 17:55:18.441480_unknown.csv"
        self.ana_nmf = Analyzer(file_name, file_unknown,small=small)

        file_name = "results/OKAPI_2019-04-29 17:55:32.779216.csv"
        file_unknown = "results/OKAPI_2019-04-29 17:55:32.779216_unknown.csv"
        self.ana_okapi = Analyzer(file_name, file_unknown,small=small)

        self.total = self.ana_w2v.total
    def evaluate(self):
        self.predictions = []
        for i in range(self.ana_nmf.total):
            vote = self.__vote(i)

            if vote:
                self.predictions.extend([vote])
            else:
                vote = self.__get_conf_vote(i)


    def __get_conf_vote(self,index):

        w2v = self.get_confidence(self.ana_w2v.get_distance(index))
        lsa = self.get_confidence(self.ana_lsa.get_distance(index))
        nmf = self.get_confidence(self.ana_nmf.get_distance(index))
        okapi = self.get_confidence(self.ana_okapi.get_distance(index))

        conf = [w2v, lsa, nmf, okapi]
        predictons = [self.ana_w2v.get_prediction(index),self.ana_lsa.get_prediction(index),self.ana_nmf.get_prediction(index),self.ana_okapi.get_prediction(index)]

        maxes = np.argwhere(conf == np.max(conf))
        choice = np.random.choice(maxes.flatten(), 1)

        return predictons[choice[0]]

    def __vote(self,index):
        w2v = self.ana_w2v.get_prediction(index)
        lsa = self.ana_lsa.get_prediction(index)
        nmf = self.ana_nmf.get_prediction(index)
        okapi = self.ana_okapi.get_prediction(index)

        votes = [w2v,lsa,nmf,okapi]
        count = [votes.count(0),votes.count(1),votes.count(2),votes.count(3)]

        maxes = np.argwhere(count == np.max(count))
        if len(maxes.flatten()) > 1:
            return None
        else:
            print("agreed on:",maxes.flatten()[0])
            return maxes.flatten()[0]


    def get_confidence(self,distances):
        if distances:
            one = distances[0] + distances[1] + distances[3]
            two = distances[0] + distances[2] + distances[4]
            three = distances[1] + distances[2] + distances[5]
            four = distances[3] + distances[4] + distances[5]

            dist = [one, two, three, four]
            maxes = np.argwhere(dist == np.max(dist))
            choice = np.random.choice(maxes.flatten(), 1)

            d = dist[choice[0]]
            dist.remove(d)
            maxes = np.argwhere(dist == np.max(dist))
            second_choice = np.random.choice(maxes.flatten(), 1)

            confidence = d / dist[second_choice[0]]
            return confidence
        else:
            return 0

    def get_acc(self):
        return self.predictions.count(3)/self.total

    def get_acc_error(self):
        acc = self.get_acc()
        err = np.sqrt( acc * (1 - acc) / self.total)
        return err