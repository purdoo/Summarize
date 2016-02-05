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
  t = textToSentences('Another place where wandering bishops abounded was the ancient Christian missionary territory of southern India, where, according to local tradition, the greatest and most vigorous of all wandering bishops, Apostle Thomas, lies in a tomb not far from the city of Madras. The Christians of St Thomas, originally Brahmins from the Malabar coast, continued for centuries as a fiercely independent series of communities, forever asserting their rights against popes and patriarchs who claimed jurisdiction over them. And so it came to pass that the stubborn Dutch Old Catholics and the factious South Indian Christians became the unpremeditated progenitors of independent, or wandering, bishops, who are now numbered in the thousands and are spread over every continent of the globe. The initiators of this unprecedented proliferation were two priests, one English, the other French-American, who, in the latter part of the nineteenth and early part of the twentieth centuries received consecration at the hands of representatives of the Dutch and South Indian Catholic bishops. They were Arnold Harris Matthew (1852-1919) and Joseph René Vilatte (1854-1929), respectively. Matthew became the leading prelate of the Old Catholic Church in Great Britain, while Vilatte brought the stream of the originally Syrian succession of the South Indian church to the United States. Not bound by traditional rules and restrictions regarding the consecrations of other bishops, these two free-lance prelates proceeded to lay their anointed hands on a goodly number of men on both sides of the Atlantic, and thus initiated a new era in the history of wandering bishops.')
  p = findProperNouns(t)
  condensePluralForms(p)
