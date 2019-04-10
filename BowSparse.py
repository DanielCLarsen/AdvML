from sklearn.feature_extraction.text import CountVectorizer
import sys
import json
import csv
from progress_bar import progress_bar
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
            csv.field_size_limit(sys.maxsize)
            with open(wiki_data_path+"_vocab.json",encoding="utf8") as vocab_file:
                self.vocab = json.load(vocab_file)

            #bow = CountVectorizer(vocabulary=self.vocab)

            with open(wiki_data_path, 'r',encoding="utf8") as wiki_file:
                reader = csv.reader(wiki_file)
                max_articles = int(next(reader)[0])
                pb = progress_bar(max_articles, title="loading data into bow")
                articles = []
                for row in reader:
                    if row:
                        articles.append(row[0])
                        pb()

            bow = CountVectorizer()
            X = bow.fit_transform(articles)
            self.__dump(X,self.vocab,output_file_path)


    def __dump(self,sparse_matrix,vocab,filename):
        scipy.sparse.save_npz(filename, sparse_matrix)
        with open(filename+"_vocab.json",'w') as f:
            json.dump(vocab,f)

    def __load(self,filename):
        with open(filename+"_vocab.json",'r') as f:
            self.vocab = json.load(f)
        return scipy.sparse.load_npz(filename+".npz")