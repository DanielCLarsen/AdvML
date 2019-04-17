from sklearn.feature_extraction.text import CountVectorizer
import sys
import json
import csv
from utils.progress_bar import progress_bar
import os
import scipy.sparse


class BowSparse():
    def __init__(self,path_to_bow=os.path.join("embeddings","bow"),
                 wiki_data_path=os.path.join("data","wiki_dk_clean.csv"),
                 overwrite=False):
        if os.path.isfile(path_to_bow+".npz") and not overwrite:
            print("loading bow from: ",path_to_bow)
            self.bow = self.__load(path_to_bow)
        else:
            print("Bow not found at: ",path_to_bow)
            print("Creating bow first")
            self.__create(wiki_data_path=wiki_data_path,output_file_path=path_to_bow)

            print("loading bow from: ", path_to_bow)
            self.bow = self.__load(path_to_bow)

    def __call__(self):
        return self.bow

    def __create(self,wiki_data_path=os.path.join("data","wiki_dk_clean.csv"),
                 output_file_path = os.path.join("embeddings","bow")):

        if not os.path.isfile(wiki_data_path):
            raise Exception("Path for clean wiki file is not valid: ",wiki_data_path)

        if os.path.isfile(output_file_path+"npz"):
            print("Output file already exist, skipping creating bow")
            print("output path:", output_file_path)
        else:
            #TODO windows proof this
            csv.field_size_limit(sys.maxsize)

            with open(wiki_data_path, 'r',encoding="utf8") as wiki_file:
                reader = csv.reader(wiki_file)
                max_articles = int(next(reader)[0])
                pb = progress_bar(max_articles, title="loading data into bow")
                articles = []
                for row in reader:
                    if row:
                        articles.append(row[0])
                        pb()

            bow = CountVectorizer(token_pattern=r'\b[\S0-9]+\b')
            X = bow.fit_transform(articles)
            print(bow.get_feature_names()[:100])

            self.vocab = self.__create_vocab(bow.get_feature_names())
            self.__dump(X,self.vocab,output_file_path)


    def __dump(self,sparse_matrix,vocab,filename):
        scipy.sparse.save_npz(filename, sparse_matrix)
        with open(filename+"_vocab.json",'w',encoding="utf8") as f:
            json.dump(vocab,f)

    def __load(self,filename):
        with open(filename+"_vocab.json",'r',encoding="utf8") as f:
            self.vocab = json.load(f)
        return scipy.sparse.load_npz(filename+".npz")

    def __create_vocab(self,list_of_names):
        c = 0
        vocab = {}
        for word in list_of_names:
            vocab.update({word:c})
            c+=1
        return vocab