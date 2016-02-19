"""
  Methods associated with incorporating the article title or subsection titles into the Summarization algorithm
"""

def getArticleTitle(path):
  with open(path, 'r') as fin:
    title = fin.readline()
  print(title)

if __name__ == "__main__":
  getArticleTitle('Articles/Zika.txt')
