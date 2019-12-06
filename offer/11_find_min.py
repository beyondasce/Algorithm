import random

def get_min(li,left,right):
    if li[left] < li[right]:
       return li[left]
    if left == right or left > right:
       return li[left]
    mid = (left+right)/2
    if li[mid] >li[left]:
        left = mid
    elif li[mid] == li[left]:
        return min(get_min(li,left,mid),get_min(li,mid+1,right)) 
    else:
        right = mid
    return get_min(li,left,right)
        
        
    
    


if __name__ == "__main__":
    num = 20
    my_list = [ random.randint(0,50) for i in range(num)]
    my_list = sorted(my_list)
    index = random.randint(0,num)
    new_list = my_list[index:] + my_list[:index]
    print(new_list)
    num = get_min(new_list,0,len(new_list)-1)
    print(num)
