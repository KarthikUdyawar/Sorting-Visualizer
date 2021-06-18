import time

def merge(data,drawData, l, m, r):
    
    n1 = m - l + 1
    n2 = r- m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = data[l + i]

    for j in range(0 , n2):
        R[j] = data[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        data[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        data[k] = R[j]
        j += 1
        k += 1
    
    
    # l is for left index and r is right index of the
    # sub-array of arr to be sorted
def mergeSort(data, drawData, timer,l,r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l+(r-1))//2

        # Sort first and second halves
        mergeSort(data, drawData, timer, l, m)
        mergeSort(data, drawData, timer, m+1, r)
        merge(data, drawData, l, m, r)
        time.sleep(timer)
        # drawData(data, ['Green' if x == l else "Blue" if x == m else 'Red'  for x in range(len(data))]) 
    
    drawData(data, ['Green' for x in range(len(data))]) 