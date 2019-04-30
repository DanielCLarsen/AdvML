from utils.wiki_parser import parse_wiki_w2v
from models.FastText import FastText
from utils.evaluator import Evaluator

parse_wiki_w2v(max_articles=None,overwrite=False)

ft = FastText(ft_binaries_path="embeddings/daft.bin")

Evaluator(ft)
