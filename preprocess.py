import io 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

f = open("query-indo-eng.trec", "r")
doc_col = f.read().replace('.', '')
doc_col = doc_col.replace('?', '')
doc_col = doc_col.lower()
f.close()

f = open("query-indo-eng-out.trec", "w")
f.write(doc_col)
f.close()

print("#######")

stop_words = set(stopwords.words('english'))
f = open("query-indo-eng-out.trec") 
line = f.read()
words = line.split()
iter = 0
for r in words:
    if not r in stop_words:
        # print(r)
        # iter += 1
        # if (iter > 15):
        #     break
        appendFile = open('query-indo-eng-out-filtered.trec','a')
        appendFile.write(" "+r)
        appendFile.close()
f.close()
# f = open("../adi/query-indo-eng-out.trec", "r")
# if f.mode == "r":
#     contents = f.readlines()
#     queries = []
#     for row in contents:
#         if (row[0]!='<'):
#             queries.append(row)
