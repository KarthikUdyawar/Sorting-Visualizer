import time
def insertion_sort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >=0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b

def bucket(data, drawData, timer):
    bucket_size = 100
    min = data[0]
    max = data[0]
    for i in range(1, len(data)):
        if data[i] < min:
            min = data[i]
        elif data[i] > max:
            max = data[i]
    bucket_count = ((max - min) // bucket_size) + 1
    buckets = []
    for i in range(0, bucket_count):
        buckets.append([])
    for i in range(0, len(data)):
        buckets[(data[i] - min) // bucket_size].append(data[i])
    k = 0
    for i in range(0, len(buckets)):
        insertion_sort(buckets[i])
        for j in range(0, len(buckets[i])):
            data[k] = buckets[i][j]
            drawData(data, ['Green' if x == k else 'Red' for x in range(len(data))]) 
            time.sleep(timer) 
            k += 1
    drawData(data, ['Green' for x in range(len(data))]) 