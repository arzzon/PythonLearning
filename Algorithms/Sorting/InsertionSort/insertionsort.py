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
 *      3. Compare it(key) with elements in the sorted part
 *         3.1. If the key is less than the element in the sorted part.
 *              3.1.1. Move the element in the sorted part one place to the right.
 *              3.1.2. Move left and compare that with the key.
 *         3.2. If the key is greater than or equal to the element in consideration in the sorted part.
 *              3.2.1. stop and go to 4.
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
        while j >= 1 and arr[j-1] > key:
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

