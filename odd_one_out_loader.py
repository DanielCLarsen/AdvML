import csv
import os



def load_odd_one_out():
    f = open(os.path.join("data","four_words_2.csv"),'r')
    r = csv.reader(f)
    challenge = []
    for row in r:
        c = [row[0],row[1],row[2],row[3]]
        challenge.append(c)

    return challenge