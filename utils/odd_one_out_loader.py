import csv



def load_odd_one_out(dataset):
    f = open(dataset,'r')
    r = csv.reader(f)
    header = next(r)
    challenge = []
    for row in r:
        c = [row[0],row[1],row[2],row[3]]
        challenge.append(c)

    return challenge