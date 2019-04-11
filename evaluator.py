from odd_one_out_loader import load_odd_one_out
import os
import datetime
import csv
def evaluate(model,dataset=os.path.join("data","odd_one_out_djt.csv")):
    odd_one_out = load_odd_one_out(dataset)

    correct = 0
    know = 0
    total = 0
    unknown_words_array = []
    rowCounter = 0
    failedChallenges_array = []
    for row in odd_one_out[1:]:
        rowCounter += 1
        total += 1
        #For each word in row, check if part of model.vocab, save unknown words.
        for word in row:
            if word in model.vocab:
                unknown_words_array.append(word)

        try:
            index = model.predict(row)
            know += 1
            if index == 3:
                correct += 1
            else:
                failedChallenges_array.append(rowCounter)
        except Exception as e:
            print(e)
            continue

    print("acc", correct / total)
    print("Know", know)
    print("Dont know", 100-know)

    #Write unknown_words_array
    current_time = datetime.datetime.utcnow()
    print("Saving unknown words to file: 'folder/unknownWords_{}".format(current_time))
    myFile = open('folder/unknownWords_{}'.format(current_time), 'w',encoding="utf8")
    with myFile:
       writer = csv.writer(myFile)
       writer.writerows(unknown_words_array)

    print("Saving failed challenges to file: 'folder/failedChallenges_{}".format(current_time))
    ##Write failedChallenges_array
    current_time = datetime.datetime.utcnow()
    myFile = open('folder/failedChallenges_{}'.format(current_time), 'w', encoding="utf8")
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(failedChallenges_array)