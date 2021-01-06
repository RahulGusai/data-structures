#! /usr/bin/python3



class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def constructBinaryTree(parentArr):
    nodes = []
    for i in range(0,len(parentArr)):
        nodes.append(Node(i))

    for i in range(0,len(parentArr)):

        if parentArr[i]==-1:
            root = nodes[i]

        else:     
            if nodes[parentArr[i]].left==None:
                nodes[parentArr[i]].left = nodes[i]
            else:
                nodes[parentArr[i]].right = nodes[i]    

    return root



def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print(root.info)
        printInOrder(root.right)

parentArr = [1, 5, 5, 2, 2, -1, 3]
root = constructBinaryTree(parentArr)
printInOrder(root)
