#! /usr/bin/python
# -*- coding: utf-8 -*-

import MeCab
myMecab = MeCab.Tagger ("-Owakati -u cookpad.dic")
f = open("cookpadzenpann_corpus.txt", "r")
f2 = open("cookpadzenpann_wakati.txt", "w")
lines = f.readlines()
for line_ in lines:
    line = myMecab.parse(line_)
    f2.write(line+"\n")
f.close()