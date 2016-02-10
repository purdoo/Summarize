from nltk import tokenize #py -m pip install nltk, then run import nltk, nltk.download()
from nltk.stem.snowball import SnowballStemmer

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




if __name__ == "__main__":
  """  
  sents = textToSentences('')
  p = findProperNouns(sents)
  condensePluralForms(p)
  """
