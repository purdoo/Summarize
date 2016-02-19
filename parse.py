from nltk import tokenize
from nltk.stem.snowball import SnowballStemmer

"""
Methods for parsing articles and formatting them for the summarization algorithm
Web Scraping functions will be put here for now
"""
def loadArticleText(path):
  with open(path, 'r') as fin:
    page = fin.read()
  return textToSentences(page)

def textToSentences(text):
  return tokenize.sent_tokenize(text)

def findProperNouns(sentences):
  properNouns = {}
  for s in sentences:
    words = tokenize.word_tokenize(s)
    for w in words[1:]:
      if w[0].isupper():
        if w in properNouns:
          properNouns[w] += 1
        else:
          properNouns[w] = 1
  return properNouns

def condensePluralForms(tokens):
  for key,value in tokens.items():
    print(key)


