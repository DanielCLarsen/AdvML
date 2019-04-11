# ML GOODSTUFF

## TODO
* test new evalutor
* add index of word in incorrect answered challanges
* finish okapi

se lsa test for demo


## general guideline:
1. Use wiki parser first
2. then BOW sparse
3. put that into your favorite model
4. model is requried to have a .predict(words) function
5. put the model into evaluator
6. hope for the best


## Results
#### LSA on all articles:
* acc: 0.52
* know: 93
* dont_know: 7

Words not known: `vvs-mand, h.c., café, 60, 1864, halvsyg, slikskål`

This version of LSA does not clean the query vector. This means that it
cannot recognize any query vectors that contains any symbols. The bow used does not use any normalization.  

#### LSA on all articles numbers included:
* ('I dont know', 'h')
* ('I dont know', '60')
* ('I dont know', '1864')
* ('I dont know', 'halvsyg')
* ('I dont know', 'slikskål')

acc 0.52
know 95
dont_know 5

This version splits and cleans the query vector and numbers are included.
The feature vector of multiple words are the average of them.

###### Big dataset

* ('I dont know', 'h')
* ('I dont know', '60')
* ('I dont know', '1864')
* ('I dont know', 'halvsyg')
* ('I dont know', 'slikskål')
* ('I dont know', '20')
* ('I dont know', '5')
* ('I dont know', 'fyrvækeri')
* ('I dont know', 'mascare')
* ('I dont know', 'halsterklæde')
* ('I dont know', '200')
* ('I dont know', 'viskelædder')
* ('I dont know', 'tv2play')
* ('I dont know', 'soduku')
* ('I dont know', '24')
* ('I dont know', 'skærstorsdag')
* ('I dont know', 'trapetz')
* ('I dont know', '7')
* ('I dont know', 'tv2play')
* ('I dont know', 'å')
* ('I dont know', 'mascare')
* ('I dont know', 'halsterklæde')
* ('I dont know', 'fransbrød')
* ('I dont know', 'badevinger')

acc 0.40100250626566414
know 375
dont_know 24

#### Word2Vec on all articles with numbers
* ('I dont know', 'bæreposer')
* ('I dont know', 'håndboldekspert')
* ('I dont know', 'vuggede')
* ('I dont know', 'halvsyg')
* ('I dont know', 'sagsakt')
* ('I dont know', 'slikskål')

acc 0.73
know 94
dont_know 6

This version splits and cleans the query vector and numbers are included.
The feature vector of multiple words are the average of them.

##### big dataset

* ('I dont know', 'bæreposer')
* ('I dont know', 'håndboldekspert')
* ('I dont know', 'vuggede')
* ('I dont know', 'halvsyg')
* ('I dont know', 'sagsakt')
* ('I dont know', 'slikskål')
* ('I dont know', 'penalhus')
* ('I dont know', 'landingstel')
* ('I dont know', 'fyrvækeri')
* ('I dont know', 'ørepropper')
* ('I dont know', 'køkkenrulle')
* ('I dont know', 'mascare')
* ('I dont know', 'halsterklæde')
* ('I dont know', 'treds')
* ('I dont know', 'viskelædder')
* ('I dont know', 'tv2play')
* ('I dont know', 'pjatte')
* ('I dont know', 'badeforhæng')
* ('I dont know', 'regnjakke')
* ('I dont know', 'hje')
* ('I dont know', 'soduku')
* ('I dont know', 'køkkenrulle')
* ('I dont know', 'uldsokker')
* ('I dont know', 'skærstorsdag')
* ('I dont know', 'trapetz')
* ('I dont know', 'børnhave')
* ('I dont know', 'tv2play')
* ('I dont know', 'skruemaskine')
* ('I dont know', 'køkkenrulle')
* ('I dont know', 'mascare')
* ('I dont know', 'halsterklæde')
* ('I dont know', 'fransbrød')
* ('I dont know', 'badevinger')
* ('I dont know', 'tømre')

acc 0.6240601503759399
know 365
dont_know 34

#### NMF

* ('I dont know', 'h')
* ('I dont know', '60')
* ('I dont know', '1864')
* ('I dont know', 'halvsyg')
* ('I dont know', 'slikskål')

acc 0.46
know 95
dont_know 5

###### big dataset
* ('I dont know', 'h')
* ('I dont know', '60')
* ('I dont know', '1864')
* ('I dont know', 'halvsyg')
* ('I dont know', 'slikskål')
* ('I dont know', '20')
* ('I dont know', '5')
* ('I dont know', 'fyrvækeri')
* ('I dont know', 'mascare')
* ('I dont know', 'halsterklæde')
* ('I dont know', '200')
* ('I dont know', 'viskelædder')
* ('I dont know', 'tv2play')
* ('I dont know', 'soduku')
* ('I dont know', '24')
* ('I dont know', 'skærstorsdag')
* ('I dont know', 'trapetz')
* ('I dont know', '7')
* ('I dont know', 'tv2play')
* ('I dont know', 'å')
* ('I dont know', 'mascare')
* ('I dont know', 'halsterklæde')
* ('I dont know', 'fransbrød')
* ('I dont know', 'badevinger')

acc 0.42606516290726815
know 375
dont_know 24



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


