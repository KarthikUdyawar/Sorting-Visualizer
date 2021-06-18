import time
def radix(data, drawData, timer):
    def counting_sort(exp):
        output = [0] * len(data)
        count = [0] * (10)
        for i in range(0, len(data)):
            idx = (data[i]//exp)
            count[int((idx)%10)] += 1
        for i in range(1,10):
            count[i] += count[i-1]
        i = len(data)-1
        while i >= 0:
            idx = (data[i]/exp)
            output[count[int((idx)%10)]-1] = data[i]
            count[int((idx)%10)] -= 1
            i -= 1
            drawData(data, ['Green' if x == i+1 else 'Red' for x in range(len(data))])  
            time.sleep(timer)
        i = 0
        for i in range(len(data)):
            data[i] = output[i]
            
    maximum = max(data)
    exp = 1
    while maximum // exp > 0:
        counting_sort(exp)
        exp *= 10
        
    drawData(data, ['Green' for x in range(len(data))]) 
