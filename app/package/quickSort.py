import time
def quick(data,drawData,timer, start, end):
    if len(data) == 1:
        return data
    if start < end:
        pivot = partition(data,drawData,timer,start,end)
        quick(data,drawData,timer,start,pivot-1)
        quick(data,drawData,timer,pivot+1,end)
        # time.sleep(timer)
        drawData(data, ['Green' for x in range(len(data))]) 

def partition(data,drawData,timer, start, end):
    
    i = start-1
    x = data[end]
    for j in range(start, end):
        if data[j] <= x:
            i += 1
            data[i], data[j] = data[j], data[i]
            time.sleep(timer)
            # drawData(data, ['Green' if x == i else 'Red' for x in range(len(data))]) 
    data[i+1], data[end] = data[end], data[i+1]
    # drawData(data, ['Green' for x in range(len(data))])
    return i+1