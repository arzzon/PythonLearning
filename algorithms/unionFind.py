''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of Union Find datastructure.
 *
 *  Written:       27/1/2019
 *  Last updated:  27/1/2019
 *
 *  % python unionFind.py
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

if __name__ == "__main__":
    uf = UnionFind(5)
    uf.unify(0,1)
    uf.unify(2,1)
    uf.unify(4,3)
    print("Roots after unifying:",uf.id)
    print('numComponents:',uf.getComponents())
    print('size:',uf.getTotalSize())
    print("Roots after path compression(done by find()):")
    for i in range(5):
        print(i,"=>",uf.find(i))
    print("1 is connected to 3:",uf.connected(1,3))
    print("0 is connected to 2:",uf.connected(0,2))

'''
Initially:
Indices: 0 1 2 3 4(We assume index 0 means vertex 0, index 1 means vertex 1 etc.)
roots  : 0 1 2 3 4(root vertices)
After Unifying:
Indices: 0 1 2 3 4
roots  : 1 2 2 3 3
'''