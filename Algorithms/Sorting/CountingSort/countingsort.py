''' *****************************************************************************
 *  Name:      Arbaaz Khan
 *  Language:  python3
 *
 *  Description:  Implementation of Counting sort algorithm.
 *  Mantra:
 *
 *  Written:       21/10/2019
 *  Last updated:  21/10/2019
 *
 *  TIME COMPLEXITIES:
 *  -----------------------------------------------------------------
 *  |   Operations  |   WorstCase   |  AverageCase  |    BestCase   |
 *  -----------------------------------------------------------------
 *  |   sorting     |      bigO(n)  |     bigO(n)   |    bigO(n)    |
 *  -----------------------------------------------------------------
 *
 *  % python countingsort.py
 *  % Algorithm:
 *    CountingSort(arr):
 *      1.
 *
 *      % Info:
 *      > It's only used when the elements are integers in the range 1->k where k is some integer.
***************************************************************************** '''

def CountingSort(arr):
    # Find max in arr to create temp array of size equal to max.
    max = -9999999
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    # Create temp array of size equal to max.
    temp = [0]*(max+1)
    # Now use the arr elements as the index in the temp array and increment the value in temp array to track frequency.
    for i in range(len(arr)):
        temp[arr[i]] += 1

    # Now put the elements which are the indices in temp array in the original array, keeping in mind their frequencies.
    k = 0  # For original array
    for i in range(max+1):
        if temp[i] != 0:
            for j in range(temp[i]):
                arr[k] = i
                k += 1

if __name__ == "__main__":
    arr = [5, 7, 10, 20, 2, 1, 3, 3, 2]
    CountingSort(arr)
    print(arr)

'''
OUTPUT:
[1, 2, 2, 3, 3, 5, 7, 10, 20]
'''
