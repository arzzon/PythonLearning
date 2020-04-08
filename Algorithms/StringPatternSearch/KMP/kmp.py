''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3 
 *
 *  Description:  Implementation of KMP algorithm.
 *
 *  Written:       26/2/2018
 *  Last updated:  26/2/2018
 *  
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  | prefix table  |    bigO(m)    |    bigO(m)    |    bigO(m)    |
 *  -----------------------------------------------------------------
 *  | kmp searching |   bigO(m+n)   |   bigO(m+n)   |   bigO(m+n)   |
 *  -----------------------------------------------------------------
 *
 *  MEMORY COMPLEXITY: bigO(m+n) 
 *  Memory complexity  
 *
 *  % python KMP.py
 *
***************************************************************************** '''

def buildPrefixTable(P):
    prefix_table = [0 for i in range(len(P))]
    prefix_table[0] = 0
    i = 1
    j = 0
    while i < len(P):
        if P[i] == P[j]:
            prefix_table[i] = j+1
            i += 1
            j += 1
        elif j > 0:
            j = prefix_table[j-1]
        else:
            #prefix_table[i] = 0
            i += 1
    return prefix_table

def kmp(S,P):
    prefix_table = buildPrefixTable(P)
    i = 0 #for prefix table
    j = 0 #for string
    while j < len(S):
        #print("i,j=" ,i,j)
        if S[j] == P[i]:
            i += 1
            j += 1

        if i == len(P): # Index of prefix table will only be equal to len(p) if a pattern has been matched otherwise it is always < len(p)
            print("Pattern found at index ",j-i)
            j = j - i + 1 #Check for more matches
            i = 0
        elif j < len(S) and S[j] != P[i]:
            if i != 0:
                i = prefix_table[i-1]
            else:
                j += 1
                 
if __name__ == "__main__":
    #S = "abxabcabcaby"
    #P = "abcaby"
    S="AAAAvAAhABAAAABkAAAAB"
    P="AAAAB"
    kmp(S,P)