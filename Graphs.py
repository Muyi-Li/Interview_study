class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):#time and space O(V+E)
        visited = [vertex]
        queue = [vertex]
        while queue:#O(V)
            deVertex = queue.pop(0)#first element in the list
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:#O(E)
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
    
    def dfs(self,vertex):#time and space are O(V+E)
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop() #last element in the list
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


customDict = {"a":["b","c"],
             "b":["a","d","e"],
             "c":["a","e"],
             "d":["b","e","f"],
             "e":["d","f",],
             "f":["d","e"]}

graph = Graph(customDict)
graph.addEdge("e","c")
#print(graph.gdict["e"])
#graph.bfs("a")# start with a
graph.dfs("a")