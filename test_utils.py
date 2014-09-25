import unittest

from utils import readfile
from utils import tokenize_text

class UtilsTestCase(unittest.TestCase):
    
    def test_readfile(self):
      tokens = readfile('data/test_data/sentences.txt')
      self.assertEqual(3, len(tokens))

    def test_tokenize_text(self):
      tokens = tokenize_text('data/test_data/sentences.txt',True)
      self.assertEqual(86, len(tokens))
        
if __name__ == '__main__':
  unittest.main()
