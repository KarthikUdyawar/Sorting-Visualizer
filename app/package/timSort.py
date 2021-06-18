import time
# Python3 program to perform basic timSort
MIN_MERGE = 32
 
def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.
 
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 
 
# This function sorts array from left index to
# to right index which is of size almost RUN
def insertionSort(data, drawData, timer, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and data[j] < data[j - 1]:
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1
            drawData(data, ['Green' if x == j else 'Red' for x in range(len(data))]) 
            time.sleep(timer) 
 
# Merge function merges the sorted runs
def merge(data, l, m, r):
     
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(data[l + i])
    for i in range(0, len2):
        right.append(data[m + 1 + i])
 
    i, j, k = 0, 0, l
     
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
 
        else:
            data[k] = right[j]
            j += 1
 
        k += 1
 
    # Copy remaining elements of left, if any
    while i < len1:
        data[k] = left[i]
        k += 1
        i += 1
 
    # Copy remaining element of right, if any
    while j < len2:
        data[k] = right[j]
        k += 1
        j += 1
 
 
# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def tim(data, drawData, timer):
    n = len(data)
    minRun = calcMinRun(n)
     
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(data, drawData, timer, start, end)
 
    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:
         
        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
 
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(data, left, mid, right)
 
        size = 2 * size
        # drawData(data, ['Green' if x == n + 1 else 'Red' for x in range(len(data))]) 
        
    drawData(data, ['Green' for x in range(len(data))])