import csv
import sys
from BOW import BOW_sparse,BOW
from progress_bar import progress_bar
csv.field_size_limit(sys.maxsize)


f = open("wiki_dk_clean_small.csv",'r')

r = csv.reader(f)
bow = BOW("danish")
pb = progress_bar(344000,title="loading data into bow")
for row in r:
    bow.update_text_fast(row[0],row[1])
    pb()

bow.exlude(5)

bow.dump("bow_wiki_clean_small.csv")