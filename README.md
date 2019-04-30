# ML GOODSTUFF

## general guideline:
1. Use wiki parser first
2. then BOW sparse
3. put that into your favorite model
4. model is requried to have a .predict(words) function
5. put the model into evaluator
6. hope for the best


## Results
| Large dataset (399)| LSA    | NMF   | Okapi BM25   | Word2Vec  | FastText | Ensemble | Human | Random |
|-----------|--------|-------|--------------|-----------|-----------|-----------|-----------|-----------|
| accuracy  | 42.6% ± 2.4% | 45.1% ± 2.5% | 69.4% ± 2.3% | 64.2% ± 2.4%| 71.2% ± 2.3% | 50.4% ± 2.5% | | 25.0% ± 2.2% |


| Small dataset (100)| LSA    | NMF   | Okapi BM25   | Word2Vec  | FastText | Ensemble | Human | Random |
|-----------|--------|-------|--------------|-----------|-----------|-----------|-----------|-----------|
| accuracy  | 49.0% ± 5.0% | 47.0% ± 5.0% | 71.0% ± 4.5% | 73.0% ± 4.4%|85.0% ± 3.6%|53.0% ± 5.0%| 97.0% ± 0%|25.0% ± 4.3%|



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


