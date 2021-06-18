import time
def bubble(data,drawData,timer):
        # print(self.data,self.drawData,self.timer,self.isAinmation,self.interupt)
        # print("Into module")
        # print(data,drawData,timer,isAinmation,interupt)
        # print("Into interupt")
        n = len(data)
        
        for i in range(n):
            for j in range(0,n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j] 
                    
                    drawData(data, ['Green' if x == j + 1 else 'Red' for x in range(len(data))]) 
                    time.sleep(timer) 
            
        drawData(data, ['Green' for x in range(len(data))]) 