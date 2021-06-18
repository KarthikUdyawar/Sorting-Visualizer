import time
def shell(data, drawData, timer):
    gap = len(data) // 2
    while gap > 0:
        for i in range(gap,len(data)):
            temp = data[i]
            j = i
            while j >= gap and data[j-gap] > temp:
                data[j] = data[j-gap]
                j -= gap
                drawData(data, ['Green' if x == j else 'Red' for x in range(len(data))])
                time.sleep(timer)
            data[j] = temp
        gap //= 2
    drawData(data, ['Green' for x in range(len(data))]) 