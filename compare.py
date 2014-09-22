import argparse
import logging
import constants
import os
import utils
#process input files for comparison
def process_files(first_file,second_file):
  tokens_1 = utils.readfile(first_file)
  tokens_2 = utils.readfile(second_file)
  print tokens_1
  

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


