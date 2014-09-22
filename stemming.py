from nltk.stem.porter import *
import nltk
import os
import re
import argparse

def readfile(input_file):

  ins = open(input_file,'r')
  array = []
  for line in ins:
    zz = re.sub('[^A-Za-z0-9+-.]+',' ', line.lower())
    array.append(zz)

  all_tokens = []

  for line in array:
    tokens = nltk.word_tokenize(line)
    line_tokens = []
    for token in tokens:
      if(not(token.isspace())):
        line_tokens.append(token)
    if line_tokens:
      all_tokens.append(line_tokens)
  return all_tokens

def stem():
  stemmer = PorterStemmer()
  stemmer.stem(token)
