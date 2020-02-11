import io 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

import os

f = open('query-indo-eng.trec', 'r')
doc_col = f.read().replace('.', '')
doc_col = doc_col.replace('?', '')
doc_col = doc_col.replace(',', '')
doc_col = doc_col.lower()
f.close()

f = open('query-indo-eng-out.trec', 'w')
f.write(doc_col)
f.close()


stop_words = set(stopwords.words('english'))
f = open("query-indo-eng-out.trec") 
line = f.read()
words = line.split()
if (os.path.exists('query-indo-eng-out-filtered.trec')):
    os.remove('query-indo-eng-out-filtered.trec')
for r in words:
    if not r in stop_words:
        if (r.endswith('>')):
            appendFile = open('query-indo-eng-out-filtered.trec','a')
            if (r.startswith('</')):
                appendFile.write('\n' + r + '\n')
            else:
                appendFile.write(r + '\n')
            appendFile.close()
        else:
            appendFile = open('query-indo-eng-out-filtered.trec','a')
            appendFile.write(r+' ')
            appendFile.close()
f.close()
f = open('query-indo-eng-out-filtered.trec', 'r')
if f.mode == 'r':
    contents = f.readlines()
    queries = []
    for row in contents:
        if (row[0]!='<'):
            queries.append(row)
