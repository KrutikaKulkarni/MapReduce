 
#!/usr/bin/python
import sys

currentWord = None
author = None
dict = {}
# stdin input
for line in sys.stdin:
  #Remove leading and trailing whitespaces
    line = line.strip()
  # parse the that we got from mapper.py
    title = line.split('\t')[1]
    title = title.strip()	
    author = line.split('\t')[0]
    author = word.strip()
		
if author in dict:
    if title not in dict[author]:
              dict[author][title]=1
    else:
	dict[author][title]+=1
			
else:
    dict[author] = {}
    dict[author][title]=1

# do not forget to output the last word if needed!
if current_Word == author:
    if title in dict:
        if title not in dict[author] :
            dict[author][title]=1
	else:
	    dict[author][title]+=1
else :
    dict[author] = {}
    dict[author][title]=1

for author in dict:
    print"{0} \t {1}\n".format(author,dict[author]))
