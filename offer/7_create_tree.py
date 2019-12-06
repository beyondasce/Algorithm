class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def create_tree(qian,zhong):
    if not qian:
       return
    # print(qian,zhong)
    v1 = qian[0]
    n1 = Node(v1)
    z_index = zhong.index(v1)
    z_left = zhong[:z_index]
    z_right = zhong[z_index+1:]
    # print(z_left,z_right)

    max = 0
    for i in z_left:
        index = qian.index(i)
        if index >max:
           max = index
    qian_left = qian[1:max+1]
    qian_right = qian[ max+1:]
    n1.left = create_tree(qian_left,z_left)
    n1.right = create_tree(qian_right,z_right)
    return n1

def qian_gui(tree):
    if not tree:
        return
    print(tree.value)
    qian_gui(tree.left)
    qian_gui(tree.right)

def for_qian(tree):
    if not tree:
        return
    t1 = tree
    stack = []
    while stack or t1:
        while t1:
            print(t1.value)
            stack.append(t1)
            t1 = t1.left
        t2 = stack.pop(-1)
        t1 = t2.right

def zhong_gui(tree):
    if not tree:
        return 
    zhong_gui(tree.left)
    print(tree.value)
    zhong_gui(tree.right)


def for_zhong(tree):
    if not tree:
       return
    stack = []
    t1 = tree
    while stack or t1:
          while t1:
              stack.append(t1)
              t1 = t1.left
          p2 = stack.pop(-1)
          print(p2.value)
          t1 = p2.right

def hou_gui(tree):
    if not tree:
        return
    hou_gui(tree.left)
    hou_gui(tree.right)
    print(tree.value)

def for_hou(tree):
    if not tree:
       return
    stack1 = []
    stack2 = []
    t1 = tree
    while stack1 or t1:
        while t1:
           stack1.append(t1)
           stack2.append(t1.value)
           t1 = t1.right
 
        t2 = stack1.pop(-1)
        t1 = t2.left
    for i in stack2[::-1]:
        print(i) 
    
def ceng_tree(tree):
    if not tree:
        return
    stack = [tree]
    while stack:
        t1 = stack.pop(0)
        print(t1.value)
        if t1.left:
            stack.append(t1.left)
        if t1.right:
            stack.append(t1.right)

def ceng_tree_2(tree):
    if not tree:
        return
    stack = [tree,None]
    ceng = 1
    a = 0
    while stack:
        if a ==2:
           break
        t1 = stack.pop(0)
        if t1:
          a = 0
          print(t1.value,ceng)
          if t1.left:
              stack.append(t1.left)
          if t1.right:
              stack.append(t1.right)
        else:
          a +=1
          stack.append(None)
          ceng += 1
           
          
    
def ceng_tree_z(tree):
    if not tree:
        return
    stack = [tree,None]
    stack2 = []
    ceng = 1
    a = 0
    while stack:
        if a ==2:
           break
        t1 = stack.pop(0)
        if t1 and ceng%2==0:
          a = 0
          print(t1.value)
          if t1.left:
              stack.append(t1.left)
          if t1.right:
              stack.append(t1.right)
        elif t1 and ceng%2==1:
          a = 0
          stack2.append(t1.value)
          if t1.left:
              stack.append(t1.left)
          if t1.right:
              stack.append(t1.right)
          
        else:
          while stack2:
             print(stack2.pop(-1))
          a +=1
          stack.append(None)
          ceng += 1



if __name__ == "__main__":
    qian = [1,6,2,7,8,5,3] # 前
    zhong = [2,7,6,1,5,8,3] # 中 
    print(qian)
    print(zhong)
    p = create_tree(qian,zhong)
    # qian_gui(p)
    # for_qian(p)

    # zhong_gui(p)
    # print("===================")
    # for_zhong(p)
    
    hou_gui(p)
    print("===================")
    for_hou(p)
    print("===================")
    ceng_tree(p)
    print("===================")
    ceng_tree_2(p)
    print("===================")
    ceng_tree_z(p)
    print("6666666666")
   

    
    
        
