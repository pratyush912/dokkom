from nltk.stem.porter import *
import nltk
import os
import re
import argparse

def readfile(input_file):

  ins = open(input_file,'r')
  array = []
  for line in ins:
    zz = re.sub('[^A-Za-z0-9\+]+',' ', line.lower())
    array.append(zz)

  stemmer = PorterStemmer()

  stemmed_tokens = []

  for line in array:
    tokens = nltk.word_tokenize(line)
    for token in tokens:
      stemmed_tokens.append(stemmer.stem(token))
      #print stemmer.stem(token)
    #print '----------------------------------------------------------' 
  return stemmed_tokens

#parser = argparse.ArgumentParser(description='Pass an input file')
#parser.add_argument('-i','--input-file', help='Input file', required=True)
#args= parser.parse_args()
#input_file = args.input_file

