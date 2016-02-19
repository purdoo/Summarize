from nltk import tokenize #py -m pip install nltk, then run import nltk, nltk.download()
from nltk.stem.snowball import SnowballStemmer
import sentenceGraph as SG
import parse

"""
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
"""

def summarize(path, depth):
  text = parse.loadArticleText('Articles/Zika.txt')
  summaryBot = SG.SentenceGraph()
  order = 1
  for t in text:
    sNode = SG.SentenceNode(order)
    sNode.addContent(t)
    summaryBot.addNode(sNode)
    order += 1
  summaryBot.compareSentences()
  #summaryBot.showEdges()
  summaryBot.rankSentences(depth)
  print(summaryBot.selected)
  summaryBot.showSummary()
  
if __name__ == "__main__":
  summarize('Articles/Zika.txt', 3)
