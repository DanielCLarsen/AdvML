# ML GOODSTUFF

se lsa test for demo


## general guideline:
1. Use wiki parser first
2. then BOW sparse
3. put that into your favorite model
4. model is requried to have a .predict(words) function
5. put the model into evaluator
6. hope for the best


##Results
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


#### NMF

* ('I dont know', 'h')
* ('I dont know', '60')
* ('I dont know', '1864')
* ('I dont know', 'halvsyg')
* ('I dont know', 'slikskål')

acc 0.46
know 95
dont_know 5
