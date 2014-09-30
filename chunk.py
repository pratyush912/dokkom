import nltk
from nltk.corpus import conll2000
import utils

def chunk_preposition(text):
  pattern = "CHUNK:{<<CD>?(?!(IN|CC|\,|\:)).*>+}"
  chunker=nltk.RegexpParser(pattern)
  result =chunker.parse(tagged)
  result.draw()
  print result

def chunk_np(tokens):
  pattern = r"""NP: {(<CD><TO>)?<DT|PP\$|CD>?<JJ.*>*<NN.*>+}
  """

  #                  {<JJ>*<NN.*>+}
  chunker=nltk.RegexpParser(pattern)
  result =chunker.parse(tokens)
  #result.draw()
  #print result
  return result

class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents): 
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]for sent in train_sents]
        self.tagger = nltk.UnigramTagger(train_data) 

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag) in zip(sentence, chunktags)]
        return nltk.chunk.util.conlltags2tree(conlltags)


class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents): 
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]for sent in train_sents]
        self.tagger = nltk.BigramTagger(train_data) 

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag) in zip(sentence, chunktags)]
        return nltk.chunk.util.conlltags2tree(conlltags)
"""
text='When prototyping a feature, you should make regular checkpoint commits.'
text='His little yellow dog barked at the cat'
text='Rapunzel let down her long black hair'
text='1.  Current Job: Senior Consultant/Project Manager at MindTree Ltd. '
tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)
#chunk_preposition(tagged)
chunked = chunk_np(tagged)
#tag_sents = [nltk.chunk.tree2conlltags(tree) for tree in chunked]
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP']) 
#cp = nltk.RegexpParser("NP: {<[CDJNP].*>+}")
unigram_chunker = BigramChunker(train_sents)
print (unigram_chunker.evaluate(test_sents))
#print tag_sents
#postags = sorted(set(pos for sent in train_sents for (word,pos) in sent.leaves()))
#print(unigram_chunker.tagger.tag(postags))
"""
file_text=''
with open('input_test.txt', 'r') as content_file:
  file_text = content_file.read().decode('utf-8')

#sentences= nltk.sent_tokenize(file_text)
sentences=file_text.split('\n')
noun_phrases=[] 
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP']) 
chunker = BigramChunker(train_sents)
print (chunker.evaluate(test_sents))
for sent in sentences:
  if not sent:
    continue
  tokens = nltk.word_tokenize(sent)
  if len(tokens)>0:
    tagged = nltk.pos_tag(tokens)
    chunked = chunk_np(tagged)
    #chunked = chunker.parse(tagged)
    #chunked.draw()
    utils.traverse(chunked)
  
  """
  nps= [word for word,pos in chunked if pos == 'NP']
  if len(nps)>0:
    noun_phrases.append(nps)

  print noun_phrases
 
  """
