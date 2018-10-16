#this code splits stdin into sentences with nltk.tokenize.sent_tokenize

import sys
from nltk.tokenize import sent_tokenize # import nltk sentence tokenizer
for paragraph in sys.stdin:
    sentences = sent_tokenize(paragraph) # tokenize
    print (('\n').join(sentences)) # join the list of sentences using linebreak as sentence separator
