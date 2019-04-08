from NMF import NMF
from wiki_parser import parse_wiki
from BowSparse import BowSparse
from evaluator import evaluate

parse_wiki()

bow = BowSparse()

nmf = NMF(bow)

evaluate(nmf)