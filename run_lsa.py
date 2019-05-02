from models.BowSparse import BowSparse
from utils.wiki_parser import parse_wiki
from utils.evaluator import Evaluator
from models.LSA import LSA

parse_wiki(max_articles=None,overwrite=False,output_file_path="data/wiki_dk_clean.csv")

bow = BowSparse(overwrite=True,wiki_data_path="data/wiki_dk_clean.csv",
                path_to_bow="embeddings/bow")


lsa = LSA(bow,number_of_pc=100)



Evaluator(lsa)


