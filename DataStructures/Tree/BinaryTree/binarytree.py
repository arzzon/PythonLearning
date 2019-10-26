''' *****************************************************************************
 *  TODO: proper implementation with all the functions
 *  Name:      Arbaaz Khan
 *  Language:  python3
 *
 *  Description:  Implementation of binary tree.
 *
 *  Written:       26/10/2019
 *  Last updated:  26/10/2019
 *
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   insertion   |    bigO(-)    |  bigO(-)   |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   deletion    |    bigO(-)    |  bigO(-)   |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   traversal   |    bigO(-)    |    bigO(-)    |    bigO(-)    |
 *  -----------------------------------------------------------------
 *  |   searching   |    bigO(-)    |  bigO(-)   |    bigO(-)    |
 *  -----------------------------------------------------------------
 *
 *  % python binarytree.py
 *
***************************************************************************** '''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BT(object):
    def __init__(self):
        self.root = None

    def newNode(self, data):
        return Node(data)

    #def traverse(self):
    # have to implement the same way as we did for level order traversal

if __name__ == "__main__":
    bt = BT()
    bt.root = bt.newNode(5)
    bt.root.left = bt.newNode(1)
    bt.root.right = bt.newNode(7)
    bt.root.left.left = None
    bt.root.left.right = None
    bt.root.right.left = bt.newNode(2)
    bt.root.right.right = bt.newNode(3)

'''
BT:
         5
      1     7
          2   3

'''