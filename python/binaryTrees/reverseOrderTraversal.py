#! /usr/bin/python3



class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def reverseOrderTraversal(root):
    stack = []
    queue = []

    queue.append(root)

    while len(queue)>0:
        node = queue.pop(0)
        stack.append(node)

        if node.right is not None:
            queue.append(node.right)

        if node.left is not None:
            queue.append(node.left)

    while(len(stack)>0):
        print(stack.pop().data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

reverseOrderTraversal(root)