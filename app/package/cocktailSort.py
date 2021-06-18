import time
def cocktail(data, drawData, timer):
    swapped = True
    start = 0
    end = len(data) - 1
    while swapped == True:
        swapped = False
        for i in range(start, end):
            if (data[i] > data[i+1]):
                data[i], data[i+1] = data[i+1], data[i]
                drawData(data, ['Green' if x == i + 1 else 'Red' for x in range(len(data))]) 
                time.sleep(timer) 
                swapped = True
        if swapped == False:
            break
        swapped == False
        end -= 1
        for i in range(end-1, start-1, -1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                drawData(data, ['Green' if x == i + 1 else 'Red' for x in range(len(data))]) 
                time.sleep(timer) 
                swapped = True
        start += 1
    drawData(data, ['Green' for x in range(len(data))]) 