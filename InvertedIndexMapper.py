#!/usr/bin/env python
import sys
import re
import os
import string

try:
    filename = os.environ['mapreduce_map_input_file']
except KeyError:
    filename = os.environ['map_input_file']

filename = filename.split('/')[-1]


for line in sys.stdin:
    line = line.lower()
    line = line.split()
    for word in line:
      word = word.strip()
      word = word.translate(None, string.punctuation)
      if len(word) > 1:
	 print "{0} \t {1}".format(word,filename)
