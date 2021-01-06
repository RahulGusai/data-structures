#! /usr/bin/python3

class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None

    
def inOrderRecursion(root):
    if root is not None:
        inOrderRecursion(root.left)
        print(root.info)
        inOrderRecursion(root.right)

def inOrderWithoutRecursion(root):
    stack = []
    current=root

    while current!=None or len(stack)>0:
        while(current!=None):
            stack.append(current)
            current=current.left
                
        poppedNode = stack.pop()
        print(poppedNode.info)

        current = poppedNode.right



root  = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(8)
# inOrderRecursion(root)
inOrderWithoutRecursion(root)

