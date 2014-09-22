import re
import nltk

#reads and input file and tokenizes all the lines
#returns and array of tokenized lines
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
