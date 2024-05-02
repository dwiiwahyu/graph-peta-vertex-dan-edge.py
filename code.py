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

  
myGraph = Graph()
myGraph.masukanVertex("BANDUNG")
myGraph.masukanVertex("SUBANG")
myGraph.masukanVertex("INDRAMAYU")
myGraph.masukanVertex("CIREBON")
myGraph.masukanVertex("TEGAL")
myGraph.masukanVertex("PEMALANG")
myGraph.masukanVertex("PURWOKERTO")
myGraph.masukanVertex("CILACAP")
myGraph.masukanVertex("BANJAR")
myGraph.masukanVertex("TASIKMALAYA")
myGraph.masukanVertex("KUNINGAN")
myGraph.masukanVertex("SUMEDANG")
myGraph.masukanEdge("BANDUNG","SUBAG")
myGraph.masukanEdge("BANDUNG","INDRAMAYU")
myGraph.masukanEdge("BANDUNG","CIREBON")
myGraph.masukanEdge("BANDUNG","TEGAL")
myGraph.masukanEdge("BANDUNG","PEMALANG")
myGraph.masukanEdge("BANDUNG","PURWOKERTO")
myGraph.masukanEdge("BANDUNG","CILACAP")
myGraph.masukanEdge("BANDUNG","BANJAR")
myGraph.masukanEdge("BANDUNG","TASIKMALAYA")
myGraph.masukanEdge("BANDUNG","KUNINGAN")
myGraph.masukanEdge("BANDUNG","SUMEDANG")
myGraph.masukanEdge("SUBANG","INDRAMAYU")
myGraph.masukanEdge("SUBANG","CIREBON")
myGraph.masukanEdge("SUBANG","TEGAL")
myGraph.masukanEdge("SUBANG","PEMALANG")
myGraph.masukanEdge("SUBANG","PURWOKERTO")
myGraph.masukanEdge("SUBANG","CILACAP")
myGraph.masukanEdge("SUBANG","BANJAR")
myGraph.masukanEdge("SUBANG","TASIKMALAYA")
myGraph.masukanEdge("SUBANG","KUNINGAN")
myGraph.masukanEdge("SUBANG","SUMEDANG")
myGraph.masukanEdge("INDRAMAYU","CIREBON")
myGraph.masukanEdge("INDRAMAYU","TEGAL")
myGraph.masukanEdge("INDRAMAYU","PEMALANG")
myGraph.masukanEdge("INDRAMAYU","PURWOKERTO")
myGraph.masukanEdge("INDRAMAYU","CILACAP")
myGraph.masukanEdge("INDRAMAYU","BANJAR")
