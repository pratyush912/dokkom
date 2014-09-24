import argparse
import logging
import constants
import os
import utils
import nltk
from nltk import metrics


"""
total steps-
  - token comparison
"""

def fuzzy_comparison(tokens_1,tokens_2,max_dist=1):
  """ compares the tokens based on fuzzy match """
  for token in reversed(tokens_1):
    if len(token)<=2:
      continue
    for tkn in reversed(tokens_2):
      if len(tkn)<=2:
        continue
      if metrics.edit_distance(token, tkn) <= max_dist:
        print "Match found for:"+token+" - "+tkn
	tokens_2.remove(tkn)
	tokens_1.remove(token)
	break



def token_comparison(tokens_1,tokens_2):
  """compares input based on token matches irrespective of order"""
  init_term_1 = len(tokens_1)
  init_term_2 = len(tokens_2)
  for token in reversed(tokens_1):
    try:
      tokens_2.remove(token)
      logging.debug("Value "+token+" removed successfully") 
      tokens_1.remove(token)
    except ValueError:
      logging.debug("Value "+token+" does not exist in second array")
  len_of_1 = len(tokens_1)
  len_of_2 = len(tokens_2)
  score_1 = (init_term_1 - len_of_1)/float(init_term_1)
  score_2 = (init_term_2 - len_of_2)/float(init_term_2)
  if len_of_2 ==0 and len_of_1==0:
    print "Both the documents are exact matches"
  else:
    if len_of_2==0:
      print "Second document is completely matching first document but the first document has "+str(len_of_1)+" different term(s)"
    elif len_of_1==0:
      print "First document is completely matching second document but the second document has "+str(len_of_2)+" different term(s)"
    else:
      print "Initial terms for first document were "+str(init_term_1)+"\nInitial terms for second document were "+str(init_term_2)+"\nSecond document has "+str(len_of_2)+" different term(s)"+"\nFirst document has "+str(len_of_1)+" different term(s)"
  return score_1, score_2

def process_files(first_file,second_file):
  """process input files for comparison"""
  tokens_1 = utils.tokenize_text(first_file)
  tokens_2 = utils.tokenize_text(second_file)
  tc_scr1,tc_scr2 = token_comparison(tokens_1,tokens_2)
  print "First-->Second Score:"+str(tc_scr1) + " Second-->First Score-->"+str(tc_scr2)

#logging configuration
logging.basicConfig(filename='app.log',level=constants.LOG_LEVEL)

#adding argument parser
parser = argparse.ArgumentParser(description='Pass input files')
parser.add_argument('-ff','--first-file', help='First Input file', required=True)
parser.add_argument('-fs','--second-file', help='Second Input file', required=True)

args= parser.parse_args() #parsing arguments
first_input_file = args.first_file
second_input_file = args.second_file
logging.debug('First Input File:'+first_input_file)
logging.debug('Second Input File:'+second_input_file)

#validating arguments for file exists
if os.path.isfile(first_input_file) and os.path.isfile(second_input_file):
  logging.debug('Valid files')
  process_files(first_input_file,second_input_file)
else:
  logging.error('Invalid input file..')  


