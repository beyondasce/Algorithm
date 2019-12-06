#encoding= utf-8
class TreeNode():
    ceng_list = []
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None 
    def S_Xian(self,node):
       if node == None:
           return
       print node.value
       self.S_Xian(node.left)
       self.S_Xian(node.right)
    def T_Zhong(self,node):
       if node == None:
           return
       self.T_Zhong(node.left)
       print node.value
       self.T_Zhong(node.right)
    def T_Hou(self,node):
       if node == None:
           return
       self.T_Hou(node.left)
       self.T_Hou(node.right)
       print node.value
        
    def S_Ceng(self,node):
       while node or  TreeNode.ceng_list:
           if node == None:
              node = TreeNode.ceng_list.pop(0) 
              continue
           print node.value
           TreeNode.ceng_list.append(node.left)
           TreeNode.ceng_list.append(node.right)
           node = TreeNode.ceng_list.pop(0)
        
class  SpinTree():
    def Mirror(self,node):
        if node == None:
            return
        self.Mirror(node.left)
        self.Mirror(node.right)
        node.left,node.right = node.right,node.left
if __name__ == "__main__":
    a = TreeNode("a")
    b = TreeNode("b")
    c = TreeNode("c")
    d = TreeNode("d")
    e = TreeNode("e")
    f = TreeNode("f")
    g = TreeNode("g")
    h = TreeNode("h")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left =h
    sp = SpinTree()
    print '---------------------------------------------'
    print '旋转树'
    sp.Mirror(a)
    print '---------------------------------------------'
    Tr = TreeNode(None)
    print '先根树'
    Tr.S_Xian(a)
    print '---------------------------------------------'
    print '中根树'
    Tr.T_Zhong(a)
    print '---------------------------------------------'
    print '后根树'
    Tr.T_Hou(a)
    print '---------------------------------------------'
    print '层次树'
    Tr.S_Ceng(a)
    print '---------------------------------------------'

    
