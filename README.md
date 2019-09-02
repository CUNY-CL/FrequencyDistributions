This directory contains various linguistic frequency distributions, represented
by two-column TSV files where the first column is the linguistic representation
(usually, though not always, a token or word) and the second its frequency.

The [LNRE calculator](https://gist.github.com/kylebgorman/445f0143f43c1751f824af7140c1df04)
can ingest these files and produce useful descriptive statistics.

# Table of contents

* Tweets by [`@dril`](https://twitter.com/dril):
  - Token
    [frequencies](dril.tsv),
    [summary](dril.txt)
* Yahoo! Horoscopes, 2010:
  - Token unigram
    [frequencies](horoscpes-1.tsv),
    [summary](horoscopes-1.txt)
  - Token bigram
    [frequencies](horoscopes-2.tsv),
    [summary](horoscopes-2.txt)
  - Token trigram
    [frequencies](horoscopes-3.tsv),
    [summary](horoscopes-3.txt)
* The bible, King James Version:
  - Token
    [frequencies](kjv.tsv),
    [summary](kjv.txt)
* English News Crawl, 2017:
  - Token
    [frequencies](news.2017-1.tsv),
    [summary](news.2017-1.txt)
* English syntax from the Wall St. Journal portion of the [Penn Treebank](https://catalog.ldc.upenn.edu/LDC99T42):
  - Word/XPOS
    ("emissions")
    [frequencies](wsj-emission.tsv),
    [summary](wsj-emission.txt)
  - Binarized and lexicalized (v = 1, h = 1) CFG rule
    ("production rule")
    [frequencies](wsj-production.tsv),
    [summary](wsj-production.txt) 
* English syntax from the [English Web Treebank](https://catalog.ldc.upenn.edu/LDC2012T13):
  - Word/dependency relation pair
    [frequencies](en_ewt-form-deprel.tsv),
    [summary](en_ewt-form-deprel.txt)
  - Word/headword pair
    ("bilexical dependency")
    [frequencies](en_ewt-form-head-form.tsv),
    [summary](en_ewt-form-head-form.txt) 
  - Word/head UPOS pair
    [frequencies](en_ewt-form-head-upos.tsv),
    [summary](en_ewt-form-head-upos.txt)
  - UPOS/headword pair
    [frequencies](en_ewt-upos-head-form.tsv),
    [summary](en_ewt-upos-head-form.txt)
* Czech morphology from [Prague Dependency Treebank](https://ufal.mff.cuni.cz/pdt3.0):
  - Token
    [frequencies](cs_pdt-token.tsv),
    [summary](cs_pdt-token.txt)
  - Lemma
    [frequencies](cs_pdt-lemma.tsv),
    [summary](cs_pdt-lemma.txt)
  - XPOS
    [frequencies](cs_pdt-xpos.tsv),
    [summary](cs_pdt-xpos.txt)
  - UPOS
    [frequencies](cs_pdt-upos.tsv),
    [summary](cs_pdt-upos.txt)
  - Universal Dependencies morphology tag
    [frequencies](cs_pdt-ud-morph.tsv),
    [summary](cs_pdt-ud-morph.txt)
  - UniMorph morphology tag
    [frequencies](cs_pdt-um-morph.tsv),
    [summary](cs_pdt-um-morph.txt)
* French phonology from [Lexique](http://www.lexique.org/):
  - Phoneme
    [frequencies](lexique.tsv),
    [summary](lexique.txt)
