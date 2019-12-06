import copy

class Solution:
    
    def __init__(self,data = []):
        self.data = data

    def maopao(self,data):
        
        data = copy.deepcopy(data) 
        for i in range(len(data)):
            for j in range(len(data)-i):
                if j+1 < len(data):
                    if data[j] > data[j+1]:
                        data[j],data[j+1] = data[j+1],data[j]
        print data

    def zhijie(self,data):
        data = copy.deepcopy(data)
        
        for i in range(len(data)):
            min = data[i]
            j_value = i 
            for j in range(i,len(data)):
                if data[j] < min:
                    min = data[j]
                    j_value = j
            data[i],data[j_value] = data[j_value],data[i]
        print data

    def insert(self,data):
        data = copy.deepcopy(data)

        for i in range(len(data)):
            for j in range(i):
                if data[i] < data[j]:
                    value = data.pop(i)
                    data.insert(j,value)
                    break

        print data

    def quick_sort(self,data,left,right):
        #data = copy.deepcopy(data)
        if left < right:
            mid = self.partition(data,left,right)
            self.quick_sort(data,left,mid-1)
            self.quick_sort(data,mid+1,right)
        

    def partition(self,data,left,right):
        value = data[left]
        while left < right:
            while data[right] >= value and left < right:
                right -= 1
            data[left] = data[right]
            while data[left] <= value and left < right:
                left += 1
            data[right] = data[left]
        data[left] = value
        return left



                
         
                   
            
                    
                   

if __name__=="__main__":
    s = Solution()

    data = [30,20,30,13,25,7,100,22,34,63,32,62,52,44,66,33,30,3,5]

    s.maopao(data)
    print '-----------------------------------------------'
    s.zhijie(data)
    print '-----------------------------------------------'
    s.insert(data)
    print '-----------------------------------------------'
    
    print data
    s.quick_sort(data,0,len(data)-1)
    print data
