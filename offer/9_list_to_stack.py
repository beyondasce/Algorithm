class my_stack():

    def __init__(self):
        self.l1 = []
        self.l2 = []
        self.num = 0
    def push(self,value):
        a = self.l1 if self.l1 else self.l2
        a.append(value)
        self.num += 1

    def pop(self):
        if not self.num:
            raise Exception("----------")
        a1 = self.l1 if self.l1 else self.l2
        b1 = self.l2 if self.l1 else self.l1
        self.num -= 1
        n = self.num
        while n>0:
            b1.append(a1.pop(0))
            n -= 1
        value = a1.pop(0)
        return value

    def __str__(self):
        a1 = self.l1 if self.l1 else self.l2
        if a1:
            return " ".join([str(x) for x in a1])

if __name__ == "__main__":
    stack = my_stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack)
    stack.pop()
    print(stack)
    
           
        
       
