def getNum(n): #因为python中int是无限大的，所以这个方式不行
    num = 0
    temp :int  = 1
    while temp:#因为python中int是无限大的，所以这个方式不行
        # print(temp)
        if n& temp:
            num += 1
        temp:int = temp << 1 
    return num

def getRightNum(n):# 如果输入的是负数会存在问题
    num = 0 
    while n:
        num += 1
        n = n &(n-1)
    return num


if __name__ == "__main__":
    # print(getNum(1))
    print(getRightNum(-1))
