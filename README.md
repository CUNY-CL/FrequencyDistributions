This directory contains various linguistic frequency distributions, represented
by two-column TSV files where the first column is the linguistic representation
(usually, though not always, a token or word) and the second its frequency.

The [LNRE calculator](https://ist.github.com/kylebgorman/445f0143f43c1751f824af7140c1df04)
can ingest these files and produce useful descriptive statistics.

# Table of contents

* Tweets by [`@dril`](https://twitter.com/dril):
  - Token
    [frequencies](frequencies/dril.tsv),
    [summary](summary/dril.txt),
    [graph](graph/dril.png)
* Yahoo! Horoscopes, 2010:
  - Token unigram
    [frequencies](frequencies/horoscpes-1.tsv),
    [summary](summary/horoscopes-1.txt),
    [graph](graph/horoscopes-1.png)
  - Token bigram
    [frequencies](frequencies/horoscopes-2.tsv),
    [summary](summary/horoscopes-2.txt),
    [graph](graph/horoscopes-2.png)
  - Token trigram
    [frequencies](frequencies/horoscopes-3.tsv),
    [summary](summary/horoscopes-3.txt),
    [graph](graph/horoscopes-3.png)
* The bible, King James Version:
  - Token
    [frequencies](frequencies/kjv.tsv),
    [summary](summary/kjv.txt),
    [graph](graph/kjv.png)
* English News Crawl, 2017:
  - Token
    [frequencies](frequencies/news.2017-1.tsv),
    [summary](summary/news.2017-1.txt),
    [graph](graph/news.2017-1.png)
* English syntax from the Wall St. Journal portion of the [Penn Treebank](https://catalog.ldc.upenn.edu/LDC99T42):
  - Word/XPOS
    ("emissions")
    [frequencies](frequencies/wsj-emission.tsv),
    [summary](summary/wsj-emission.txt),
    [graph](graph/wsj-emission.png)
  - Binarized and lexicalized (v = 1, h = 1) CFG rule
    ("production rule")
    [frequencies](frequencies/wsj-production.tsv),
    [summary](summary/wsj-production.txt),
    [graph](graph/wsj-production.png) 
* English syntax from the [English Web Treebank](https://catalog.ldc.upenn.edu/LDC2012T13):
  - Word/dependency relation pair
    [frequencies](frequencies/en_ewt-form-deprel.tsv),
    [summary](summary/en_ewt-form-deprel.txt),
    [graph](graph/en_ewt-form-deprel.png)
  - Word/headword pair
    ("bilexical dependency")
    [frequencies](frequencies/en_ewt-form-head-form.tsv),
    [summary](summary/en_ewt-form-head-form.txt),
    [graph](graph/en_ewt-form-head-form.png) 
  - Word/head UPOS pair
    [frequencies](frequencies/en_ewt-form-head-upos.tsv),
    [summary](summary/en_ewt-form-head-upos.txt),
    [graph](graph/en_ewt-form-head-upos.png)
  - UPOS/headword pair
    [frequencies](frequencies/en_ewt-upos-head-form.tsv),
    [summary](summary/en_ewt-upos-head-form.txt),
    [graph](graph/en_ewt-upos-head-form.png)
* Czech morphology from [Prague Dependency Treebank](https://ufal.mff.cuni.cz/pdt3.0):
  - Token
    [frequencies](frequencies/cs_pdt-token.tsv),
    [summary](summary/cs_pdt-token.txt),
    [graph](graph/cs_pdt-token.png)
  - Lemma
    [frequencies](frequencies/cs_pdt-lemma.tsv),
    [summary](summary/cs_pdt-lemma.txt),
    [graph](graph/cs_pdt-lemma.png)
  - XPOS
    [frequencies](frequencies/cs_pdt-xpos.tsv),
    [summary](summary/cs_pdt-xpos.txt),
    [graph](graph/cs_pdt-xpos.png)
  - UPOS
    [frequencies](frequencies/cs_pdt-upos.tsv),
    [summary](summary/cs_pdt-upos.txt),
    [graph](graph/cs_pdt-upos.png)
  - Universal Dependencies morphology tag
    [frequencies](frequencies/cs_pdt-ud-morph.tsv),
    [summary](summary/cs_pdt-ud-morph.txt),
    [graph](graph/cs_pdt-ud-morph.png)
  - UniMorph morphology tag
    [frequencies](frequencies/cs_pdt-um-morph.tsv),
    [summary](summary/cs_pdt-um-morph.txt),
    [graph](graph/cs_pdt-um-morph.png)
* French phonology from [Lexique](http://www.lexique.org/):
  - Phoneme
    [frequencies](frequencies/lexique.tsv),
    [summary](summary/lexique.txt),
    [graph](graph/lexique.png)
