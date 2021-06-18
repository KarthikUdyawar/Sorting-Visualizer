
# Python program for implementation of Bogo Sort
import random,time
  
# Sorts array a[0..n-1] using Bogo sort
def bogo(data, drawData, timer):
    n = len(data)
    while (is_sorted(data)== False):
        shuffle(data, drawData, timer)
    drawData(data, ['Green' for x in range(len(data))])
  
# To check if array is sorted or not
def is_sorted(data):
    n = len(data)
    for i in range(0, n-1):
        if (data[i] > data[i+1] ):
            return False
    return True
  
# To generate permutation of the array
def shuffle(data, drawData, timer):
    n = len(data)
    for i in range (0,n):
        r = random.randint(0,n-1)
        data[i], data[r] = data[r], data[i]
        drawData(data, ['Green' if x == i else 'Red' for x in range(len(data))]) 
        time.sleep(timer)