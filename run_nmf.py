from models.NMF import NMF
from utils.wiki_parser import parse_wiki
from models.BowSparse import BowSparse
from utils.evaluator import Evaluator

parse_wiki()

bow = BowSparse()

nmf = NMF(bow)

Evaluator(nmf)