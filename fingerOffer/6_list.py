import random


class My_list():
    def __init__(self,value):
        self.value = value
        self.next = None


def get_list(li):
    p = None
    p1 = p
    for i in li:
        n1 = My_list(i)
        if not p:
           p = n1
           p1 = p
        else:
           p1.next = n1
           p1 = p1.next
    return p

def digui_list(li):
    if not li:
       return
    digui_list(li.next)
    print(li.value)


def show_num(p_list):
    l1 = []
    p = p_list
    while p:
          l1.append(p.value)
          p = p.next
    l2 = []
    while l1:
        l2.append(l1.pop(-1))
    return l2
    



if __name__ == "__main__":
    l1 = [ random.randint(0,12) for i in range(12) ]
    print(l1)
    p_list = get_list(l1)
    l2 = show_num(p_list)
    
    print(l2)
    digui_list(p_list)
