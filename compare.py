import argparse
import logging
import constants

#logging configuration
logging.basicConfig(filename='app.log',level=constants.LOG_LEVEL)

#adding argument parser
parser = argparse.ArgumentParser(description='Pass an input files')
parser.add_argument('-ff','--first-file', help='First Input file', required=True)
parser.add_argument('-fs','--second-file', help='Second Input file', required=True)

args= parser.parse_args() #parsing arguments
first_input_file = args.first_file
second_input_file = args.second_file

logging.debug('First Input File:'+first_input_file)
logging.debug('Second Input File:'+second_input_file)

