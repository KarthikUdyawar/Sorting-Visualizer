import time 

def insertion(data, drawData, timer):
    for i in range(len(data)):
        j = i
        nxt_element = data[i]
        # Compare the current element with next one
		
        while (data[j-1] > nxt_element) and (j > 0):
            data[j] = data[j-1]
            j=j-1
            time.sleep(timer) 
            drawData(data, ['Green' if x == j else "Yellow" if x == i else 'Red' for x in range(len(data))])            
        data[j] = nxt_element
    
    drawData(data, ['Green' for x in range(len(data))]) 