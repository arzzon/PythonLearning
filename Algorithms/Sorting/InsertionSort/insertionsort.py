''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3
 *
 *  Description:  Implementation of Insertion sort algorithm.
 *  Mantra:       Choose an element from the unsorted half, insert it in its correct place in the sorted half.
 *
 *  Written:       20/10/2019
 *  Last updated:  20/10/2019
 *
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   sorting     |   bigO(n^2)   |   bigO(n^2)   |    bigO(n)    |
 *  -----------------------------------------------------------------
 *
 *  % python insertionsort.py
 *  % Algorithm:
 *    InsertionSort(arr):
 *      1. Start from the 2nd element considering the 1st element is in sorted part and already sorted.
 *      2. Choose one element from the unsorted part of the array
 *      3. Compare it with elements in the sorted part & shift them right till we get the correct place for the chosen element.
 *      4. Insert the chosen element in it's correct place.
 *      5. Repeat 2-5 till we have all sorted.
 *
 *  % Info:
 *      > It's inplace sorting.
 *      > Doesn't scale well.
 *      > Practically more efficient than selection and bubble sorts, even though all of them
 *        have O(n^2) worst case complexity
***************************************************************************** '''
def InsertionSort(arr):
    l = len(arr)
    # Optimized
    for i in range(1, l):
        key = arr[i]
        j = i
        while arr[j-1] > key and j >= 1:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
    return arr
if __name__ == "__main__":
    print(InsertionSort([1, -1, 2, 3, 10, -10, 2, 3, 100, 5, 7]))

#My first approach
'''
    for i in range(1, l):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j] :
            # Shift Right
            arr[j+1] = arr[j]
            j -= 1
        if j != i-1:
            arr[j+1] = key
'''

