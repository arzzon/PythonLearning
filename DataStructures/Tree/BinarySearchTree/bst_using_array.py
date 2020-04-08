''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3
 *
 *  Description:  Implementation of binary search tree.
 *
 *  Written:       30/12/2018
 *  Last updated:  30/12/2018
 *
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   insertion   |    bigO(n)    |  bigO(logn)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *  |   deletion    |    bigO(n)    |  bigO(logn)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *  |   traversal   |    bigO(n)    |    bigO(n)    |    bigO(n)    |
 *  -----------------------------------------------------------------
 *  |   searching   |    bigO(n)    |  bigO(logn)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *
 *  % python bst.py
 *
***************************************************************************** '''

def createBST(ele)

ele = list(map(int,input().strip().split(",")))



'''
BST BEFORE REMOVING ELEMENTS
         5
      3     6
    1         8
      2     7
           7

BST AFTER REMOVING ELEMENTS
AFTER REMOVING 2
         5
      3     6
    1         8
            7
           7
AFTER REMOVING 6
         5
      3     8
    1      7
          7
AFTER REMOVING 5
         3
      1     8
           7
          7
AFTER REMOVING 9
         3
      1     8
           7
          7

'''