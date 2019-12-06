class Node:
    def __init__(self,val=-1):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = Node()

    def add(self,data):
        node = Node(data)
        if self.root.val == -1:
            self.root = node
        else:
            stack = [self.root]
            while stack:
                root = stack.pop(0)
                if not root.left :
                    root.left = node
                    return
                elif not root.right:
                    root.right = node
                    return
                else:
                    stack.append(root.left)
                    stack.append(root.right)


    def xian_G(self,root):
        if root == None:
            return
        print root.val
        self.xian_G(root.left)
        self.xian_G(root.right)

    def xian_F(self,root):
        if root == None:
            return
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                print root.val
                root = root.left
            po = stack.pop(0)
            root = po.right       

    def zhong_G(self,root):
        if root == None:
            return
        self.zhong_G(root.left)
        print root.val
        self.zhong_G(root.right)


    def zhong_F(self,root):
        if root ==None:
            return
        stack =[]
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            po = stack.pop()
            print po.val
            root =po.right

    def hou_G(self,root):
        if root ==None:
            return
        self.hou_G(root.left)
        self.hou_G(root.right)
        print root.val

    def hou_F(self,root):
        if root == None:
            return
        stack1 = []
        stack2 = []

        while stack1 or root:
            while root:
                stack1.append(root)
                stack2.append(root)
                root = root.right
            le = stack1.pop()
            root = le.left

        while stack2:
            print stack2.pop().val
   
    def ceng(self,root):
        if root == None:
            return
        stack = [root]
        while stack :
            root = stack.pop(0)
            print root.val
            if root.left !=None:
                stack.append(root.left)
            if root.right != None:
                stack.append(root.right)
            
                
            




if __name__ =="__main__":
    tree = Tree()
    tree_list = [1,2,3,4,5,6,7,8]
    for data in tree_list:
        tree.add(data)

    tree.xian_G(tree.root)
    print '++++++++++++++++++++'
    tree.xian_F(tree.root)        
    
    print '--------------------------------------------'
    tree.zhong_G(tree.root)
    print '++++++++++++++++++++'
    tree.zhong_F(tree.root)


    print '--------------------------------------------'
    tree.hou_G(tree.root)
    print "+++++++++++++++++++"
    tree.hou_F(tree.root)


    print '___________________________________________'
    tree.ceng(tree.root)
