def power(base,expon):
    if base == 0 and expon<0:
        return 0
    if expon ==0:
        return 1
    result = 1
    while abs(expon):
        result *= base
        expon -= 1
    if expon<0:
        result = 1/result
    return result

def getresult(base,expon):
    if base == 0 and expon<0:
        return 0
    if expon == 0:
        return 1
    if expon == 1:
        return base
    result = fastpower(base,abs(expon))
    if expon < 0:
        result = 1/result
    return result

def fastpower(base,expon):
    if expon == 0:
        return 1
    if expon == 1:
        return base
    result = fastpower(base,expon>>1)
    result *= result
    if expon & 1:
        result *= base
    return result
    

if __name__ == "__main__":
    result = power(2,1000)
    print(result)
    result1 = getresult(2,1000)
    print(result1)
        
