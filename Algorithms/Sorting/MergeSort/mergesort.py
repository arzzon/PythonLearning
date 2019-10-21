''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3
 *
 *  Description:  Implementation of Merge sort algorithm.
 *  Mantra:       Divide the array into sub arrays and then merge.
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
 *  % python mergesort.py
 *  % Algorithm:
 *    MergeSort(arr, lb, ub):
 *      1. Divide the array into sub arrays till we have sub array with a single element left.
 *      2. Recursion terminating condition lb < ub, as when we have lb == ub, it means that we have a single element.
 *      3. Calculate mid to divide the array into two halves, mid = (lb + ub)//2
 *      4. Call merge sort recursively to divide the array, for left sub array => MergeSort(arr, lb, mid)
 *      5. For right sub array => MergeSort(arr, mid+1, ub)
 *      6. Merge the sub arrays => Merge(arr, lb, mid, ub)
 *    Merge(arr, lb, mid, ub):
 *      1. [3,5,6] [1,2]
 *          i       j
 *      2. temp array: [0, 0, 0, 0, 0] of len(arr)
 *         k = lb       k
 *      3. Till i <= mid and j <= ub
 *         if arr[i] < arr[j]
 *              temp[k] = arr[i] => put the smaller among the two in the temp array
 *              increment i and k
 *         else
 *              temp[k] = arr[j]
 *              increment j and k
 *      4. If any of the elements are left copy those into temp in the end till k reaches ub
 *      5. Copy temp from lb to ub into original array from lb to ub.
 *
 *      % Info:
 *      > Merge sort is an example of the divide and conquer strategy.
***************************************************************************** '''
def Merge(arr, lb, mid, ub):
    i = lb
    j = mid+1
    k = lb
    temp = [0 for i in range(len(arr))]
    while i <= mid and j <= ub:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    if i > mid:
        while j <= ub:
            temp[k] = arr[j]
            j += 1
            k += 1
    elif j > ub:
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
    for i in range(lb, ub + 1):
        arr[i] = temp[i]

def MergeSort(arr, lb, ub):
    if lb < ub:
        mid = (lb + ub)//2
        MergeSort(arr, lb, mid)
        MergeSort(arr, mid+1, ub)
        Merge(arr, lb, mid, ub)

if __name__ == "__main__":
    arr = [1, -1, 2, 3, 10, -10, 2, 3, 100, 5, 7]
    MergeSort(arr, 0, len(arr)-1)
    print(arr)

'''
OUTPUT:
[-10, -1, 1, 2, 2, 3, 3, 5, 7, 10, 100]
'''
