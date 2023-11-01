class Graph:
    def __init__(self):
        self.numberofnodes = 0
        self.adjacentlist = {}

    def __str__(self):
        return str(self.__dict__)

    def addVertex(self, node):
        self.adjacentlist[node] = []
        self.numberofnodes += 1

    def addEdge(self, node_one, node_two):
        self.adjacentlist[node_one].append(node_two)
        self.adjacentlist[node_two].append(node_one)
    
    def showConnections(self):
        for vertex, neighbors in self.adjacentlist.items():
            print(vertex, end ='==>')
            print(' '.join(neighbors))

mygraph = Graph()
mygraph.addVertex('0')
mygraph.addVertex('1')
mygraph.addVertex('2')
mygraph.addVertex('3')
mygraph.addVertex('4')
mygraph.addVertex('5')
mygraph.addVertex('6')
mygraph.addEdge('3', '1')
mygraph.addEdge('3', '4')
mygraph.addEdge('4', '2')
mygraph.addEdge('4', '5')
mygraph.addEdge('1', '2')
mygraph.addEdge('1', '0')
mygraph.addEdge('0', '2')
mygraph.addEdge('6', '5')

print(mygraph)
mygraph.showConnections()