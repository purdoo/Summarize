class SentenceGraph:
  graphVertices = [] # the graph vertices are simply SentenceNode objects  
  graphEdges = {} # key = (nodeA.order, nodeB.order) | value = weight  
  def __init__(self):
    pass

  def addNode(self, node):
    self.graphVertices.append(node)
  
  def updateConnection(self, a, b, weight):
    if((a,b) in self.graphEdges):
      self.graphEdges[(a,b)] += weight
    else:
      self.graphEdges[(a,b)] = weight

  def showVertices(self):
    print(self.graphVertices) # currently prints objects
  def showEdges(self):
    print(self.graphEdges)

class SentenceNode:
  score = 0
  def __init__(self, order):
    self.order = order

  def addContent(self, content):
    self.content = content

  def displayContent(self):
    return self.content

if __name__ == "__main__":
  sentenceA = SentenceNode(1)
  sentenceB = SentenceNode(2)
  sentenceC = SentenceNode(3)
  sentenceA.addContent('My name is Chris Liow.')
  sentenceB.addContent('Sometimes I stay in the office after hours to work on personal projects.')
  sentenceC.addContent('This is a graph theory implementation to evaluate the \'relatedness\' of sentences.')
  
  testGraph = SentenceGraph()
  testGraph.addNode(sentenceA)
  testGraph.addNode(sentenceB)
  testGraph.addNode(sentenceC)
  
  testGraph.updateConnection(1,2,5)
  testGraph.updateConnection(1,3,3)
  testGraph.updateConnection(1,2,1)
  #testGraph.showVertices()  
  testGraph.showEdges()
  
