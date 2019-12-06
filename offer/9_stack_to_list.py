class my_list:
     def __init__(self):
         self.l1 = [] #入
         self.l2 = [] #出
    
     def put(self,value):
         self.l1.append(value)
 
     def pop(self):
         if self.l2:
            return self.l2.pop(-1)
         while self.l1:
            self.l2.append(self.l1.pop(-1))
         if self.l2:
            return self.l2.pop(-1)
         else:
            raise Exception(".......")


if __name__ == "__main__":
    a = my_stack()
    a.put(1)
    a.put(2)
    a.put(3)
    a.put(4)
    a.put(5)
    a.put(6)
    print(a.pop())
    a.put(6)
    a.put(6)
    print(a.pop())
    print(a.pop())
    a.put(6)
    print(a.pop())
    a.put(7)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())

