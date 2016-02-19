import itertools

class SentenceGraph:
  graphVertices = [] # the graph vertices are simply SentenceNode objects  
  graphEdges = {} # key = (nodeA.order, nodeB.order) | value = weight (int or float) 
  sentenceScores = {} # key = SentenceNode order (int) | value = score (int or float) 
  ranks = {}  
  selected = []
  def __init__(self):
    pass

  def addNode(self, node):
    self.graphVertices.append(node)

  def updateConnection(self, a, b, weight):
    if((a,b) in self.graphEdges):
      self.graphEdges[(a,b)] += weight
    else:
      self.graphEdges[(a,b)] = weight    

  def compareSentences(self):
    for a,b in itertools.combinations(self.graphVertices, 2):
      # currently does not weight sentence length
      commonWords = set.intersection(set(a.content.split(' ')), set(b.content.split(' ')))
      self.updateConnection(a.order, b.order, len(commonWords))

  def rankSentences(self, factor):
    for V in self.graphVertices:
      for key in self.graphEdges:       
        if V.order in key:
          if V.order in self.ranks:
            self.ranks[V.order] += self.graphEdges[key]
          else:
            self.ranks[V.order] = self.graphEdges[key]
    for x in range(factor):    
      highScore = 0    
      index = 0    
      for k,v in self.ranks.items():
        if v > highScore:
          highScore = v
          index = k
      self.ranks.pop(index, None)      
      self.selected.append(index)
    self.selected.sort()

  def showSummary(self):
    for index in self.selected:
      print(self.graphVertices[index].content)

  def showVertices(self):
    #print(self.graphVertices) # currently prints objects
    print("Graph Vertices")
    for v in self.graphVertices:
      print(v.content)
  
  def showEdges(self):
    print(self.graphEdges)

"""
  def filterEdges(self, factor): # should be renamed or repurposed as filterEdges  
    edgeIndexes = []
    for x in range(factor):    
      highScore = 0    
      edge = (0,0)    
      for k,v in self.graphEdges.items():
        if v > highScore:
          highScore = v
          edge = k        
      self.graphEdges.pop(edge, None)      
      edgeIndexes.append(edge)
    return edgeIndexes
"""



class SentenceNode:
  score = 0
  def __init__(self, order):
    self.order = order

  def addContent(self, content):
    self.content = content

  def displayContent(self):
    return self.content







def test():
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
  testGraph.showEdges()

def commonTest():
  A = SentenceNode(1)
  B = SentenceNode(2)
  C = SentenceNode(3)
  D = SentenceNode(4)
  A.addContent('Today in the city I saw a cat chasing a rat around on the street')
  B.addContent('The cat could not catch the rat because the cat was too fat')
  C.addContent('I felt bad because the cat was sad')
  D.addContent('You never know what you will find in the city')
  testGraph = SentenceGraph()
  testGraph.addNode(A)
  testGraph.addNode(B)
  testGraph.addNode(C)
  testGraph.addNode(D)
  testGraph.compareSentences()
  testGraph.showEdges()
  #print(testGraph.filterEdges(2))
  
if __name__ == "__main__":
  commonTest()
  
