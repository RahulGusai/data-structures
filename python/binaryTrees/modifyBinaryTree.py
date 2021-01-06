#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def modifyBinaryTree(root):
    preOrderQueue = []

    if root.left is not None:
        queue = []
        queue.append(root.left)        

        while len(queue)>0:
            node = queue.pop(0)
            preOrderQueue.append(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    if root.right is not None:
        queue = []
        queue.append(root.right)        

        while len(queue)>0:
            node = queue.pop()
            preOrderQueue.append(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    for i in range(0,len(preOrderQueue)):
        root.right = preOrderQueue[i]
        root = root.right


def traversal(root):
    while root!=None:
        print(root.info)
        root = root.right


# root  = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

root = Node(10)  
root.left = Node(8)  
root.right = Node(2)  
root.left.left = Node(3)  
root.left.right = Node(5)  

modifyBinaryTree(root)

traversal(root)