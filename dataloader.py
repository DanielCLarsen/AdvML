import os
import json
from week1.BOW import BOW




bow = BOW()

for dirname in os.listdir(os.path.join(os.path.curdir,"dk_wiki_parsed")):
    print(dirname)
    c = 0
    for filename in os.listdir(os.path.join(os.curdir,"dk_wiki_parsed",dirname)):

        with open(os.path.join(os.curdir,"dk_wiki_parsed",dirname,filename)) as file:

            print(filename)
            for doc in file:
                text = ""
                content = json.loads(doc)['lines']
                title = content[0]
                #print(title)
                for line in content:
                    text += line
                bow.update_text(title,text)
        c += 1
        if c > 20:
            break
    break


print(len(bow.bow.keys()))
print(len(bow.words))
bow.exlude(3)
bow.dump("bow.csv")