import time

def selection(data, drawData, timer):
    for i in range(len(data)): 
        min_idx = i 
        # time.sleep(timer) 
        # drawData(data, ['Green' if x == i+1 else 'Red' for x in range(len(data))]) 
        for j in range(i+1, len(data)): 
            # time.sleep(2) 
            time.sleep(timer)
            # drawData(data, ['Blue' if x == min_idx else 'Red' for x in range(len(data))])
            drawData(data, ['Green' if x == min_idx else "Blue" if x == j else "Yellow" if x == i else 'Red' for x in range(len(data))])
            if data[min_idx] > data[j]: 
                min_idx = j
                
                # drawData(data, ['Green' if x == i+1 else 'Red' for x in range(len(data))]) 
                # time.sleep(timer) 
        data[i], data[min_idx] = data[min_idx], data[i] 
        #drawData(data, ['Blue' if x == min_idx else "Green" if x == i else 'Red' for x in range(len(data))])
        
        # time.sleep(timer)
    drawData(data, ['Green' for x in range(len(data))])