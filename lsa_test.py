from BowSparse import BowSparse
from wiki_parser import parse_wiki
from evaluator import evaluate
from LSA import LSA

parse_wiki(max_articles=None,overwrite=False,output_file_path="data/wiki_dk_clean.csv")

bow = BowSparse(overwrite=True,wiki_data_path="data/wiki_dk_clean_with_symbols.csv",
                path_to_bow="embeddings/bow_symbols")


lsa = LSA(bow,number_of_pc=10)

evaluate(lsa)


