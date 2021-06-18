import time 
def heapify(data, drawData, timer,n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and data[i] < data[left]:
        largest = left
    if right < n and data[largest] < data[right]:
        largest = right
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        drawData(data, ['Green' if x == i else 'Red' for x in range(len(data))]) 
        time.sleep(timer) 
        heapify(data, drawData, timer, n, largest)

def heap(data, drawData, timer):
    n = len(data)
    for i in range(n,-1,-1):
        heapify(data, drawData, timer, n, i)
    for i in range(n-1,0,-1):
        data[i], data[0] = data[0], data[i]
        heapify(data, drawData, timer, i, 0)
    drawData(data, ['Green' for x in range(len(data))]) 