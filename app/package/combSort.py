import time

def getNextGap(gap):
    gap = (gap * 10)/13
    if gap < 1:
        return 1
    return gap

def comb(data, drawData, timer):
    n = len(data)
    gap = n
    swap = True
    while gap != 1 or swap:
        gap = getNextGap(gap)
        swap = False
        for i in range(0,n-gap):
            if data[i] > data[i+gap]:
                data[i], data[i+gap] = data[i+gap], data[i]
                drawData(data, ['Green' if x == i else 'Red' for x in range(len(data))]) 
                time.sleep(timer)
                swap = True
    drawData(data, ['Green' for x in range(len(data))])