''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3
 *
 *  Description:  Implementation of Selection sort algorithm.
 *  Mantra:       Select the smallest element & place it in its proper position each time.
 *
 *  Written:       20/10/2019
 *  Last updated:  20/10/2019
 *
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   sorting     |   bigO(n^2)   |   bigO(n^2)   |    bigO(n^2)  |
 *  -----------------------------------------------------------------
 *
 *  % python selectionsort.py
 *  % Algorithm:
 *    SelectionSort(arr):
 *      1. Find the minimum value in the list(keep track of the index)
 *      2. Swap it with the value in the current position in the iteration.
 *      3. Repeat this process for all the elements until the entire array is sorted
 *
 *  % Info:
 *      > It's better over bubble sort in terms of swap operations with a total of n swaps max.
 *      > It's inplace sorting.
 *      > Doesn't scale well.
 *      > Selection sort works well for small files. It is used
 *        for sorting the files with very large values and small keys. This is because selection is made
 *        based on keys and swaps are made only when required.
***************************************************************************** '''

def SelectionSort(arr):
    l = len(arr)
    for i in range(l):
        min_index = i
        for j in range(i, l):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i: #Swap only when required, that is when min_index is not i
            #swap
            arr[i] += arr[min_index]
            arr[min_index] = arr[i] - arr[min_index]
            arr[i] = arr[i] - arr[min_index]
    return arr

if __name__ == "__main__":
    print(SelectionSort([1, -1, 2, 3, 10, -10, 2, 3, 100, 5, 7]))

