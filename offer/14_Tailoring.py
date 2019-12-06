def main(n):
    tep = {}
    return getMaxNum(tep,n)

 
def getMaxNum(tep,n):
    if 0<=n<=3:
        tep[n] = n
    if tep.get(n):
        return tep[n]
    max = 0
    for i in range(1,n//2+1):
        result = getMaxNum(tep,i) * getMaxNum(tep,n-i)
        if result > max:
            max = result
    tep[n] = max
    return tep[n]

if __name__ == "__main__":
    print(main(6))
        

    

            
