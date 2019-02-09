''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of Kruskal's algorithm.
 *
 *  Written:       28/1/2019
 *  Last updated:  28/1/2019
 *
 *  % python kruskalsAlgo.py
 *
***************************************************************************** '''

class UnionFind(object):
    def __init__(self,totalSize):
        self.totalSize = totalSize #Total number of vertices in the UnionFind
        self.numComponents = totalSize #
        self.id = [i for i in range(totalSize)] #Initially each vertex is the root of itself.
        self.size = [1 for i in range(totalSize)] #Size of each component initially is 1

    def getTotalSize(self):
        return self.totalSize

    def getComponents(self):
        return self.numComponents

    def find(self,v):
        #This function returns the root of the inquired node and at the same time does path compression.
        #Path compression: Here the root of the component is made the root of the vertex so that we can
        #check whether for some vertices belong to the same component in bigO(1) time.

        root = v
        while root != self.id[root]:#It finds the root of the component(root => the vertex would be the root of itself)
            root = self.id[root]

        while self.id[v] != root:#Path compression, root of the component is assigned as the root of all the vertices of the component
            next = self.id[v]
            self.id[v] = root
            v = next

        return root

    def unify(self,u,v):
        rootU = self.id[u]
        rootV = self.id[v]

        if rootU == rootV: #If root of both the vetices are same then they already belong to same component, so no need to unify.
            return
        
        if self.size[rootU] < self.size[rootV]: #If the size of component with rootU is smaller than that with rootV then we assign rootU as the root of the other component
            self.id[rootV] = rootU          #That means we merge the larger components with the smaller components
            self.size[rootV] += self.size[rootU] #The size of the attached component is added to the size of the component to which it is attached
        else:
            self.id[rootU] = rootV 
            self.size[rootV] += self.size[rootU] #The size of the attached component is added to the size of the component to which it is attached

        self.numComponents -= 1 #Since we merged two components, decrease the component count by 1

    def connected(self,u,v): #Checks if vertices are connected/belong to same component or not
        if self.find(u) == self.find(v): #If root of both vertices are same then return True(find() returns the root of the vertex)
            return True
        return False

class Graph(object):
    def __init__(self, verticesNum, directed = False, weighted = False):
        self.vertices = [] #Stores the vertices
        self.verticesNum = verticesNum #Number of vertices
        self.edges = [] #Stores the edges in the format [sourceVertex, destinationVertex, weight]
        self.directed = directed
        self.weighted = weighted

    def addVertex(self, id): #Stores the vertices
        self.vertices.append(id)

    def getIndex(self, vertex): #Returns the index of the vertex
        return self.vertices.index(vertex)
    
    def addEdge(self, src, dst, weight = 0):
        self.edges.append([src,dst,weight])

    def getVertices(self):
        return self.vertices

    def show(self): #Prints all the edges
        print("Edges:")
        for i in range(len(self.edges)):
            print(self.edges[i])

    def kruskalMST(self):
        self.edges = sorted(self.edges, key=lambda item: item[2]) #Sorted the edges in ascending order of the weights
        uf = UnionFind(self.verticesNum)
        resultEdges = [] #Stores the edges of the minimum spanning tree
        cost = 0 #Total weight of the minimum spanning tree
        for i in range(len(self.edges)):
            u = self.edges[i][0] #source vertex of the edge
            v = self.edges[i][1] #destination vertex of the edge
            if not uf.connected(self.getIndex(u),self.getIndex(v)): #If they don't belong to the same component then unify them
                uf.unify(self.getIndex(u),self.getIndex(v)) #The vertices are unified/merged to single component
                resultEdges.append([u,v,self.edges[i][2]]) #This edge is added to the result
                cost += self.edges[i][2]

        print(resultEdges)
        print("Cost: ",cost)
        

if __name__ == "__main__":
    g = Graph(5,False,True)
    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addEdge('a','c',5)
    g.addEdge('a','b',5)
    g.addEdge('a','d',7)
    g.addEdge('b','c',2)
    g.addEdge('b','e',8)
    g.addEdge('c','d',4)
    g.addEdge('c','e',3)
    g.addEdge('d','e',2)
    print("Vertices: "+str(g.getVertices()))
    g.show()
    print("Minimum spanning tree generated using Kruskal's algo:")
    g.kruskalMST()


'''
        5
a . . . . . . . b
. .           . .
. 5 .     2 .   .
.     .   .     .
.7      c       . 8
.     .   .     .
.  4.    3  .   .
. .           . .
d . . . . . . . e
        2
'''