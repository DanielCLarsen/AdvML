from BowSparse import BowSparse
from wiki_parser import parse_wiki
from evaluator import evaluate
from LSA import LSA

parse_wiki(max_articles=None,overwrite=False)

bow = BowSparse(overwrite=False)

lsa = LSA(bow)

evaluate(lsa)


