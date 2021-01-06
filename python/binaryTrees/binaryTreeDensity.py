#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def binaryTreeDensity(root):
    height = 1
    count = 0

    queue = []
    queue.append(root)

    while len(queue)>0:
            noOfNodes = len(queue)
            flag = False
            for i in range(0,noOfNodes):
                    node = queue.pop(0)
                    count += 1

                    if node.left!=None or node.right!=None:
                        flag = True
                    if node.left!=None:
                        queue.append(node.left)
                    if node.right!=None:
                        queue.append(node.right)
                                
            if flag==True:
                height = height+1

    print("Density of Tree = " + str(count/height))
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.left.right.left.right = Node(10)
root.right.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right = Node(7)      
root.right.right.right = Node(9)


binaryTreeDensity(root)

