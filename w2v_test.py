from wiki_parser import parse_wiki_w2v
from Word2Vec import Word2Vec
from evaluator import evaluate

parse_wiki_w2v(max_articles=None,overwrite=False)

w2v = Word2Vec()

evaluate(w2v)
