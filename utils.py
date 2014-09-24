import re
import nltk

def readfile(input_file):
  """reads and input file and tokenizes all the lines
     returns an array of tokenized lines """
  ins = open(input_file,'r')
  array = []
  for line in ins:
    zz = re.sub('[^A-Za-z0-9+-.@]+',' ', line)
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

def tokenize_text(input_file):
  """tokenizes the given input file into an array of tokens"""
  text_file = open(input_file, "r")
  text = text_file.read()
  zz = re.sub('[^A-Za-z0-9+-.@]+',' ', text.lower())
  tokens = nltk.word_tokenize(zz)
  return tokens
