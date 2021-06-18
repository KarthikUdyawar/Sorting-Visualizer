import time
def compare(data, drawData, timer, i, j, dire):
    if (dire==1 and data[i] > data[j]) or (dire==0 and data[i] < data[j]):
        data[i],data[j] = data[j],data[i]
        drawData(data, ['Green' if x == i else 'Red' for x in range(len(data))]) 
        time.sleep(timer) 

def bitonic_merge(data, drawData, timer,low, cnt, dire):
    if cnt > 1:
        k  = cnt // 2
        for i in range(low, low+k):
            compare(data, drawData, timer,i, i+k, dire)
        bitonic_merge(data, drawData, timer,low, k, dire)
        bitonic_merge(data, drawData, timer,low+k, k, dire)

def bitonic_sort(data, drawData, timer, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonic_sort(data, drawData, timer,low, k ,1)
        bitonic_sort(data, drawData, timer,low+k, k, 0)
        bitonic_merge(data, drawData, timer,low, cnt, dire)

def bitonic(data, drawData, timer):
    bitonic_sort(data, drawData, timer,0, len(data), 1)
    drawData(data, ['Green' for x in range(len(data))])