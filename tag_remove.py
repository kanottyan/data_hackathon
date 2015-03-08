#! /usr/bin/python
# -*- coding: utf-8 -*-

from django.utils import html

f = open("kijizennpann.csv", "r")
f2 = open("new_kijizennpann", "w")

lines = f.readlines()

for line in lines:
    print html.strip_tags(" ".join(line.decode('utf-8')))
