import random

def get_num(list,num):
    if not list:
       return False
    h = len(list)
    l = len(list[0])
    x = h-1
    y = 0 
    while x>=0 and y<l:
        if list[x][y] == num:
            return True
        elif list[x][y] < num:
            y += 1
        else:
            x -= 1
    return False


if __name__ == "__main__":
    list =[ [ x +2*y for x in range(10) ] for y in range(10)]
    print(list)
    print(get_num(list,26))
