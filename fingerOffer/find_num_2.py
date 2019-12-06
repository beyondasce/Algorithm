import random

def get_num(list):
    if not list:
        return False

    start = 1
    end = len(list)-1
    while start <= end:
        mid = (end + start)//2
        num = get_sum(list,start,mid)
        if end == start:
            if num > 1:
                return start
            break
        if num > (mid-start+1):
            end = mid
        else:
            start = mid +1 
    return start
            


def get_sum(list,start,end):
    n = 0
    for i in list:
        if i>= start and i <= end:
           n += 1
    return n




if __name__ == "__main__":
    list = [random.randint(1,10) for i in range(11)]
    print(list)
    print(get_num(list))
