#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def diagonalTraversal(root):

    stack = []
    temp = root
    while(temp!=None):
        stack.append(temp)
        temp = temp.right

    while len(stack)>0:
        nodes = []
        for _ in range(0,len(stack)):
            node = stack.pop(0)
            nodes.append(node)
            print(node.info,end = " ")

        print("\n")

        for node in nodes:
            node = node.left    
            while(node!=None):
                stack.append(node)
                node = node.right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)      

# root = Node(8)
# root.left = Node(3)
# root.right = Node(10)
# root.left.left = Node(1)
# root.right.left = Node(6)
# root.right.right = Node(14)      
# root.right.left.left = Node(4)
# root.right.left.right = Node(7)
# root.right.right.left = Node(13)   

diagonalTraversal(root)