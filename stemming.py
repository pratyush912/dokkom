from nltk.stem.porter import *
import nltk
import os
import re
import argparse

def readfile():

  ins = open(input_file,'r')
  array = []
  for line in ins:
    zz = re.sub('[^A-Za-z0-9\+]+',' ', line.lower())
    array.append(zz)

  stemmer = PorterStemmer()

  for line in array:
    tokens = nltk.word_tokenize(line)
    for token in tokens:
      print stemmer.stem(token)
    print '----------------------------------------------------------' 

parser = argparse.ArgumentParser(description='Pass an input file')
parser.add_argument('-i','--input-file', help='Input file', required=True)
args= parser.parse_args()
input_file = args.input_file
readfile()    

