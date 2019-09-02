This directory contains various linguistic frequency distributions, represented
by two-column TSV files where the first column is the linguistic representation
(usually, though not always, a token or word) and the second its frequency.

The [LNRE calculator](https://gist.github.com/kylebgorman/445f0143f43c1751f824af7140c1df04)
can ingest these files and produce useful descriptive statistics.

# Table of contents

* Tweets by [`@dril`](https://twitter.com/dril):
  - [Token frequencies](dril.tsv)
* Yahoo! Horoscopes, 2010:
  - [Token unigram frequencies](horoscopes-1.tsv)
  - [Token bigram frequencies](horoscopes-2.tsv)
  - [Token trigram frequencies](horoscopes-3.tsv)
* The bible, King James Version:
  - [Token frequencies](kjv.tsv)
* English News Crawl, 2017:
  - [Token frequencies](news.2017-1.tsv)
* English syntax from the Wall St. Journal portion of the [Penn Treebank](https://catalog.ldc.upenn.edu/LDC99T42):
  - [Word/language-specific POS tag frequencies](wsj-emission.tsv) ("emission frequencies")
  - [Binarized, lexicalized (v = 1, h = 1) CFG rule frequencies](wsj-production.tsv) ("production rule frequencies")
* English syntax from the [English Web Treebank](https://catalog.ldc.upenn.edu/LDC2012T13):
  - [Word/dependency relation pair frequencies](en_ewt-form-deprel.tsv)
  - [Word/headword pair frequencies](en_ewt-form-head-form.tsv) ("bilexical dependency frequencies")
  - [Word/head universal POS tag pair frequencies](en_ewt-form-head-upos.tsv)
  - [universal POS tag/headword pair frequencies](en_ewt-upos-head-form.tsv)
* Czech morphology from [Prague Dependency Treebank](https://ufal.mff.cuni.cz/pdt3.0):
  - [Token frequencies](cs_pdt-token.tsv)
  - [Lemma frequencies](cs_pdt-lemma.tsv)
  - [Language-specific POS tag frequencies](cs_pdt-xpos.tsv)
  - [Universal POS tag frequencies](cs_pdt-upos.tsv)
  - [Universal Dependencies morphology tag frequencies](cs_pdt-ud-morph.tsv)
  - [UniMorph morphology tag frequencies](cs_pdt-um-morph.tsv)
* French phonology from [Lexique](http://www.lexique.org/):
  - [Phoneme frequencies](lexique.tsv)
