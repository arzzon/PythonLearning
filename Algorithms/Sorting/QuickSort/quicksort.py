''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3
 *
 *  Description:  Implementation of Quick sort algorithm.
 *  Mantra:       Choose a pivot, Partition the array into two sub arrays and keep all the elements
 *                smaller than pivot in the left and all the elements greater than pivot to the right
 *                of the pivot, so the pivot is in it's right place, Now do the same for the left sub array
 *                and right sub array w.r.t the pivot.
 *
 *  Written:       21/10/2019
 *  Last updated:  21/10/2019
 *
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   sorting     | bigO(nlog(n)) | bigO(nlog(n)) |    bigO(-)    |
 *  -----------------------------------------------------------------
 *
 *  % python quicksort.py
 *  % Algorithm:
 *    QuickSort(arr, lb, ub):
 *      1.
 *
 *      % Info:
 *      > Mergesort is a type of quicksort where the pivot is the middle element in the array
***************************************************************************** '''

def Partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub
    while start < end:
        # Find an element that is greater than pivot
        while start < len(arr) and pivot >= arr[start]:
            start += 1
        # Find an element that is smaller than the pivot
        while end >= 0 and pivot < arr[end]:
            end -= 1
        # Swap the elements if the the indices are within the range and start < end
        if start < len(arr) and end >= 0 and start < end:
            arr[start] += arr[end]
            arr[end] = arr[start] - arr[end]
            arr[start] = arr[start] - arr[end]
    # Finally Swap arr[end] and pivot
    arr[lb] = arr[end]
    arr[end] = pivot
    return end

def QuickSort(arr, lb, ub):
    if ub > lb:
        pivot = Partition(arr, lb, ub)
        QuickSort(arr, lb, pivot-1)
        QuickSort(arr, pivot+1, ub)

if __name__ == "__main__":
    arr = [1, -1, 2, 3, 10, -10, 2, 3, 100, 5, 7]
    QuickSort(arr, 0, len(arr)-1)
    print(arr)
    
    arr = [1, 1]
    QuickSort(arr, 0, len(arr) - 1)
    print(arr)

'''
OUTPUT:
[-10, -1, 1, 2, 2, 3, 3, 5, 7, 10, 100]
'''
