"""
  Methods associated with incorporating the article title or subsection titles into the Summarization algorithm
"""

def getArticleTitle(path):
  with open(path, 'r') as fin:
    title = fin.readline()
  return title.strip()

def getTitleWords(title):
  for word in title.split(' '):
    print(word)
if __name__ == "__main__":
  title = getArticleTitle('Articles/Zika.txt')
  print(title)
  getTitleWords(title)
