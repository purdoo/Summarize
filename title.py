"""
  Methods associated with incorporating the article title or subsection titles into the Summarization algorithm

  Certain values are currently hardcoded in (such as lists for punctuation and 'empty' words) The eventual solution is to store externally or through a DB.
"""

# Hardcoded 'Lists'
punct = [',','.',':',';','\'','\"','|']
ignore = ['and', 'the', 'but', 'so', 'like', 'be', 'a','to']

def getArticleTitle(path):
  with open(path, 'r') as fin:
    title = fin.readline()
  return title.strip()

def getTitleWords(title):
  words = []
  for word in title.split(' '):
    words.append(word)
  return words

def findAbbr(title):
  pass

def reduceTitle(words):
  reduced = words  
  for word in reduced:
    for p in punct: # there has to be a more efficient way of doing this...
      word.strip(p)
    if word in ignore:
      reduced.remove(word)
  return reduced   

if __name__ == "__main__":
  title = getArticleTitle('Articles/Zika.txt')
  words = getTitleWords(title)
  print(reduceTitle(words))
