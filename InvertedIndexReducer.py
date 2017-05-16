#!/usr/bin/env python
import sys
import csv
import collections

current_word = None
word = None 
dict = {}

for line in sys.stdin:
    line = line.strip()
    word = line.split('\t')[0]
    filename = line.split('\t')[1]
    filename = filename.strip()
    if word in dict:
        if filename not in dict[word]:
	    dict[word][filename]=1
	else:
	    dict[word][filename]+=1
			
    else:
        dict[word] = {}
	dict[word][filename]=1

# do not forget to output the last word if needed!
if current_word == word:
    if word in dict :
        if filename not in dict[word]:
            dict[word][filename]=1
	else:
            dict[word][filename]+=1
else:
    dict[word] = {}
    dict[word][filename]=1

for word in dict:
    print("{0}\t{1}\n".format(word,dict[word]))
