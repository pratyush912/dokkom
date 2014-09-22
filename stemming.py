from nltk.stem.porter import *
import nltk
import os
import re

def stem(token):
  stemmer = PorterStemmer()
  return stemmer.stem(token)
