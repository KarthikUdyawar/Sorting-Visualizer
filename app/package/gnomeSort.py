import time
def gnome(data, drawData, timer):
    idx = 0
    while idx < len(data):
        if idx == 0:
            idx += 1
        if data[idx] >= data[idx - 1]:
            idx += 1
        else:
            data[idx], data[idx-1] = data[idx-1], data[idx]
            drawData(data, ['Green' if x == idx-1 else 'Red' for x in range(len(data))]) 
            time.sleep(timer) 
            idx -= 1
    drawData(data, ['Green' for x in range(len(data))]) 