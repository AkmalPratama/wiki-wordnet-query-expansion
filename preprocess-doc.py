def format_doc_adi():
    filename = 'collection/cran-ta/cran.all.1400'
    f = open(filename, 'r')
    idx = 1
    for line in f:
        trec_file = open('collection/cran-ta/cran.trec','a')
        if line.startswith('.I '):
            trec_file.write('</DOC>\n<DOC>\n<DOCNO>{}</DOCNO>\n'.format(idx))
            idx += 1
        else:
            trec_file.write(line)
        trec_file.close()
    f.close()

def format_doc_med():
    filename = 'collection/med-ta/MED.ALL'
    f = open(filename, 'r')
    idx = 1
    for line in f:
        trec_file = open('collection/med-ta/MED.trec','a')
        if line.startswith('.I '):
            trec_file.write('</DOC>\n<DOC>\n<DOCNO>{}</DOCNO>\n'.format(idx))
            idx += 1
        else:
            if not line.startswith('.W'):
                trec_file.write(line)
        trec_file.close()
    f.close()

def format_qrel():
    filename = 'collection/cran-ta/cran.qry'
    f = open(filename, 'r')
    for line in f:
        line_buf = line.split()
        qrel_file = open('collection/cran-ta/cran-qrels', 'a')
        qrel_file.write('{} 0 {} 1\n'.format(line_buf[0], line_buf[1]))
        qrel_file.close()

def format_query():
    filename = 'collection/cran-ta/cran.qry'
    f = open(filename, 'r')
    idx = 1
    for line in f:
        trec_file = open('collection/cran-ta/cran-qry.trec','a')
        if line.startswith('.I'):
            trec_file.write('</title>\n</top>\n<top>\n<num>{}</num><title>\n'.format(idx))
            idx += 1
        else:
            if not line.startswith('.W'):
                trec_file.write(line)

def format_query_cran():
    filename = 'collection/cran-ta/cran.qry'
    f = open(filename, 'r')
    idx = 1
    appended_line = ''
    for line in f:
        trec_file = open('collection/cran-ta/cran-qry-updated.trec','a')
        if line.startswith('.I'):
            if appended_line != '':
                trec_file.write(appended_line)
                appended_line = ''
            words = line.split()
            words = words[-1]
            trec_file.write('\n</title>\n</top>\n<top>\n<num>{}</num><title>\n'.format(int(words)))
            idx += 1
        else:
            if not line.startswith('.W'):
                appended_line = appended_line + ' ' + line.rstrip()
                # trec_file.write(line)

# format_doc_adi()
# format_qrel()
# format_doc_med()
# format_query()
format_query_cran()
# print(int('090'))