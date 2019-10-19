''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3
 *
 *  Description:  Implementation of Bubble sort algorithm.
 *
 *  Written:       19/1/2019
 *  Last updated:  19/1/2019
 *
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   insertion   |    bigO(n)    |     bigO(-)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *  |   deletion    |    bigO(n)    |     bigO(-)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *  |   traversal   |    bigO(n)    |     bigO(n)   |    bigO(n)    |
 *  -----------------------------------------------------------------
 *  |   searching   |    bigO(n)    |     bigO(1)   |    bigO(1)    |
 *  -----------------------------------------------------------------
 *
 *  % python bubblesort.py
 *  % Algorithm:
 *    BubbleSort(arr):
 *      1. Bubble the largest element in each iteration to the end
 *      2. track whether we are at all swapping in iteration,
            2.1. If we are not swapping in an iteration then array is sorted, stop.
 *
 *
***************************************************************************** '''
def BubbleSort(arr):
    l = len(arr) # length of array
    swap = 0 # Stops if no swap is done in an iteration(optimized)
    for i in range(0, l-1):
        swap = 0
        for j in range(i, l):
            if arr[i] > arr[j]:
                arr[i] += arr[j]
                arr[j] = arr[i] - arr[j]
                arr[i] = arr[i] - arr[j]
                swap += 1
    return arr

if __name__ == "__main__":
    print(BubbleSort([1, -1, 2, 2, 3, 4, 5, 7]))
