import nltk

def chunk_preposition(text):
  pattern = "CHUNK:{<(?!(IN|CC|\,|\:)).*>+}"
  chunker=nltk.RegexpParser(pattern)
  result =chunker.parse(tagged)
  result.draw()
  print result

def chunk_np(tokens):
  pattern = "NP: {<DT>?<JJ>*<NN.*>}"
  chunker=nltk.RegexpParser(pattern)
  result =chunker.parse(tokens)
  result.draw()
  print result



text='When prototyping a feature, you should make regular checkpoint commits.'
tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)
#chunk_preposition(tagged)
chunk_np(tagged)
