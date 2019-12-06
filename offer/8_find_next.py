class Node():
    def __init__(self,value):
       self.value = value
       self.parent = None
       self.left = None 
       self.right = None

def get_next(node):
    p_next = None
    if node.right:
       p = node.right
       while p:
           p = p.left
       p_next = p
    else:
       while p.parent and p.parent.right ==p :
           p = p.parent
       p_next = p.parent
    return p_next
           
