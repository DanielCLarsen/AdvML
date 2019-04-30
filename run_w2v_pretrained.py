from utils.wiki_parser import parse_wiki_w2v
from models.Word2Vec import Word2Vec
from utils.evaluator import Evaluator

parse_wiki_w2v(max_articles=None,overwrite=False)

w2v = Word2Vec(w2v_binaries_path="embeddings/da.bin",pretrained=True)

Evaluator(w2v)
