from BowSparse import BowSparse
from utils.wiki_parser import parse_wiki
from utils.evaluator import evaluate
from OkapiBM25 import OkapiBM25

parse_wiki(max_articles=None,overwrite=False,output_file_path="data/wiki_dk_clean.csv")

bow = BowSparse(overwrite=False,wiki_data_path="data/wiki_dk_clean.csv",
                path_to_bow="embeddings/bow")


okapi = OkapiBM25(bow)

evaluate(okapi)


