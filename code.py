class Graph:
    def __init__(self):
        self.adjList = {}
    
    def printGraph(self):
        for vertex in self.adjList:
            print(vertex, ":", self.adjList[vertex])
    
    def masukanVertex(self,vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
            return True
        return False
    
    def masukanEdge(self,v1,v2):
        if v1 in self.adjList and v2 in self.adjList:
            self.adjList[v1].append(v2)
            self.adjList[v2].append(v1)
            return True
        return False    

  
