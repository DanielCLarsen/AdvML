# ML GOODSTUFF

Dataflow:

1. wiki_parser creates clean text in "data" folder
2. either a bow or binaries for w2v or fasttext is created in "embeddings" folder
3. run scripts uses Evaluator to produce results csv file with distances and predictions
4. analyse scripts calculates accuracies and plots form the result files

#### word2vec implementation:
https://pypi.org/project/word2vec/

#### FastText implementation:
https://github.com/facebookresearch/fastText/tree/master/python

#### LSA and NMF implementation:
sklearn sparse implementation

#### Okapi BM25 implementation:c
implemented manually from the equtions on wiki:
https://en.wikipedia.org/wiki/Okapi_BM25

## Results
| Large dataset (399)| LSA    | NMF   | Okapi BM25   | Word2Vec  | FastText | FastText trained | Ensemble | Human | Random |
|-----------|--------|-------|--------------|-----------|-----------|-----------|-----------|-----------|-----------|
| accuracy  | 42.6% ± 2.4% | 45.1% ± 2.5% | 69.4% ± 2.3% | 64.2% ± 2.4%| 71.2% ± 2.3% |76.4% ± 2.1%| 50.4% ± 2.5% | | 25.0% ± 2.2% |


| Small dataset (100)| LSA    | NMF   | Okapi BM25   | Word2Vec  | FastText |FastText trained| Ensemble | Human | Random |
|-----------|--------|-------|--------------|-----------|-----------|-----------|-----------|-----------|-----------|
| accuracy  | 49.0% ± 5.0% | 47.0% ± 5.0% | 71.0% ± 4.5% | 73.0% ± 4.4%|85.0% ± 3.6%|89.0% ± 3.1%|53.0% ± 5.0%| 97.0% ± 0%|25.0% ± 4.3%|



## No model can answer:
| word 1      | word 2     | word 3   | Odd-one-out|
|------|---------|--------|--------|
| hej | hje | jeh | magi |
|kul|olie|gas|isbjørn |
|ok|okay|forstået|nej|
|Rom|Berlin|Budapest|Hamborg|
|regnjakke|paraply|regnslag|solcreme|
|gin|tonic|lime|Frugt|
|lege|spille|pjatte|seriøs|
|svømning|roning|surfing|cykling|
|ipad|iphone|ipod|computer|
|ung|gammel|barn|brun|
|påske|jul|ferie|arbejde|
|brun|grøn|rød|blomst|

## Odd-one-out highlights
Here, the harder/weirder examlpes in the expanded odd-one-out dataset are listed
### Hard questions
| word 1      | word 2     | word 3   | Odd-one-out|
|------|---------|--------|--------|
|blomst | bi|honning | hveps |
|gå	    |løbe	|kravle	|køre|
|snedker	|tømrer	|maler	|programmør|
|sjov	|humor	|grine	|trist|
|København	|Rom	|Paris	|Barcelona|
|rose	|lilje	|tulipan	|kaktus|

### Special concepts
| word 1      | word 2     | word 3   | Odd-one-out|  concept  |
|------|---------|--------|--------|--------|
|time	|sekund	|minut	|meter| time vs distance |
|20|	28|	35	|100 |(number difference)|
|fem	|5	|V	|100 |(number representation)|
|treds	|ti	|tyve	|200 |(number representation)|
|pizza	|burger	|hotdog	|salat |(junkfood)|
|vand	|juice	|mælk	|kaffe |(hot) |
|giraf	|elefant	|blåhval	|mus |(size)|
|vand	|juice	|kaffe	|øl |(alcohol)|
|hej	|hje	|jeh	|magi |(word misspelling)|
|ukendt	|uformel	|uhyggelig	|glad |(Character difference (u) )|
|solsort	|spurv	|måge	|pingvin |(cant fly)|
|uldsokker	|hjemmesko	|vinterstøvler	|sandaler |(warmth/winter)|


