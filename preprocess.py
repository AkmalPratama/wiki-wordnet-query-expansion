import io 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import os

f = open('query-indo-eng.trec', 'r')
query_col = f.read().replace('.', '')
query_col = query_col.replace('?', '')
query_col = query_col.replace(',', '')
query_col = query_col.lower()
f.close()

if not (os.path.exists('query-indo-eng-out.trec')):
    f = open('query-indo-eng-out.trec', 'w')
    f.write(query_col)
    f.close()

stop_words = set(stopwords.words('english'))
words = query_col.split()
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

f = open('query-indo-eng-out-filtered.trec', 'r')
if f.mode == 'r':
    contents = f.readlines()
    queries = []
    for row in contents:
        if (row[0]!='<'):
            queries.append(row)
f.close()

'''
import goslate

def translate_queries():
    gs = goslate.Goslate()
    ID = 'id'
    f = open('query-indo.trec', 'r')
#     text = f.readlines()
#     queries = []
#     for row in text:
#         if (row[0]!='<'):
#             queries.append(gs.translate(row,ID))
    text = f.read()
    text = gs.translate(text,ID)
    text = text.split('\n')
    queries = list(filter(lambda x: not x.startswith('<'), text))
    return queries
'''