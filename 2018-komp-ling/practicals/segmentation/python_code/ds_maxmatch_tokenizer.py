## this code inputs paths to the followin files:
## conllu file for dictionary extraction (dictionary_source)
## conllu file to test on
## name of the output file

def create_dictionary (dictionary_source):
    wordforms = set()
    openfile = open(dictionary_source,"r") 
    for line in openfile:
        splitline = line.split('\t')
        if len(splitline) > 4:
            wordform = splitline[1]
            wordforms.add(wordform)
    return wordforms
    openfile.close()

def tokenize_line (line, dictionary):
    text = re.sub (r'# text = ','', line)
    tokenized_line = ds_maxmatch.maxmatch (text, dictionary)
    return '\n'.join (tokenized_line)

def tokenize (file_with_sentences, dictionary_source, output_file):
    sentences_source = open (file_with_sentences, 'r')
    dictionary = create_dictionary (dictionary_source)
    out = open (output_file, 'w')
    for line in sentences_source:
        if 'text = ' in line:
            tokenized_line = tokenize_line(line, dictionary)
            out.write (tokenized_line)
    out.close() 
        

import sys, re, ds_maxmatch


if __name__ == '__main__':
    dictionary_source = sys.argv[1]
    file_with_sentences = sys.argv[2]
    output_file = sys.argv[3]
    tokenize (file_with_sentences, dictionary_source, output_file)





