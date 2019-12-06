import random

def find_num(list):
    if not list:
        return False
    for i in list:
        if i< 0 or i>len(list)-1:
            return False
    j = 0
    for key,value in enumerate(list):
         if key == value:
             continue
         while True:
             if key == value:
                 break
             if list[key] == list[value]:
                 print(list)
                 return list[key]
             list[key],list[value] = list[value],list[key]
             value = list[key]
    return False
        






if __name__ == "__main__":
    list = [random.randint(0,9) for x in range(10)]
    # list = [10,10,3,0,4,5,6,7,8,9]
    print(list)
    
    print(find_num(list))
