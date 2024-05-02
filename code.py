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

myGraph.masukanEdge("INDRAMAYU","TASIKMALAYA")
myGraph.masukanEdge("INDRAMAYU","KUNINGAN")
myGraph.masukanEdge("INDRAMAYU","SUMEDANG")
myGraph.masukanEdge("CIREBON","TEGAL")
myGraph.masukanEdge("CIREBON","PEMALANG")
myGraph.masukanEdge("CIREBON","PURWOKERTO")
myGraph.masukanEdge("CIREBON","CILACAP")
myGraph.masukanEdge("CIREBON","BANJAR")
myGraph.masukanEdge("CIREBON","TASIKMALAYA")
myGraph.masukanEdge("CIREBON","KUNINGAN")
myGraph.masukanEdge("CIREBON","SUMEDANG")
myGraph.masukanEdge("TEGAL","PEMALANG")
myGraph.masukanEdge("TEGAL","PURWOKERTO")
myGraph.masukanEdge("TEGAL","CILACAP")
myGraph.masukanEdge("TEGAL","BANJAR")
myGraph.masukanEdge("TEGAL","TASIKMALAYA")
myGraph.masukanEdge("TEGAL","KUNINGAN")
myGraph.masukanEdge("TEGAL","SUMEDANG")
myGraph.masukanEdge("PEMALANG","PURWOKERTO")
myGraph.masukanEdge("PEMALANG","CILACAP")
myGraph.masukanEdge("PEMALANG","BANJAR")
myGraph.masukanEdge("PEMALANG","TASIKMALAYA")
myGraph.masukanEdge("PEMALANG","KUNINGAN")
myGraph.masukanEdge("PEMALANG","SUMEDANG")
myGraph.masukanEdge("PURWOKERTO","CILACAP")
myGraph.masukanEdge("PURWOKERTO","BANJAR")
myGraph.masukanEdge("PURWOKERTO","TASIKMALAYA")
myGraph.masukanEdge("PURWOKERTO","KUNINGAN")
myGraph.masukanEdge("PURWOKERTO","SUMEDANG")
myGraph.masukanEdge("CILACAP","BANJAR")
myGraph.masukanEdge("CILACAP","TASIKMALAYA")
myGraph.masukanEdge("CILACAP","KUNINGAN")
myGraph.masukanEdge("CILACAP","SUMEDANG")
myGraph.masukanEdge("BANJAR","TASIKMALAYA")
myGraph.masukanEdge("BANJAR","KUNINGAN")
myGraph.masukanEdge("BANJAR","SUMEDANG")
myGraph.masukanEdge("TASIKMALAYA","KUNINGAN")
myGraph.masukanEdge("TASIKMALAYA","SUMEDANG")
myGraph.masukanEdge("SUMEDANG","KUNINGAN")

myGraph.printGraph()
