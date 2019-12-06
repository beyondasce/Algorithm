def get_str(str1):
    if not str1:
        return None
    list1 = list(str1)
    count =  0
    for i in list1:
        if i == ' ':
            count +=1
    list2 = [0] * (len(list1) + 2*count)
    l1 = len(list1)-1
    l2 = len(list2)-1
    while l1 != l2:
        if list1[l1] != ' ':
           list2[l2] = list1[l1]
           l1 -=1
           l2 -=1
        else:
           list2[l2] = '0'
           list2[l2-1] = '2'
           list2[l2-2] = "%"
           l2 -= 3
           l1 -= 1

    while l1 >=0:
       list2[l1] = list1[l1]
       l1 -= 1
    print(list2)   
    # return "".join([str(x) for x in range(list2)])
    return "".join(list2)


if __name__ == "__main__":
    str1 = "hello  hello world "
    print(get_str(str1))
