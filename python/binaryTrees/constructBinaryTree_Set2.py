#! /usr/bin/python3



class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def constructBinaryTree(inOrder,levelOrder):
    if len(inOrder)==1:
        return Node(inOrder[0])

    root = Node(levelOrder[0])
    for i in range(0,len(inOrder)):
        if root.info==inOrder[i]:
            break
    
    ## LST ##
    levelOrderLST = []
    for val in levelOrder:
        if val in inOrder[0:i]:
            levelOrderLST.append(val)
    ## RST ##
    levelOrderRST = []
    for val in levelOrder:
        if val in inOrder[i+1:len(inOrder)]:
            levelOrderRST.append(val)
    
    root.left = constructBinaryTree(inOrder[0:i],levelOrderLST)
    root.right = constructBinaryTree(inOrder[i+1:len(inOrder)],levelOrderRST)

    return root

def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print(root.info)
        printInOrder(root.right)




inOrder    = [ 4, 8, 10, 12, 14, 20, 22 ]
levelOrder = [ 20, 8, 22, 4, 12, 10, 14 ]

root = constructBinaryTree(inOrder,levelOrder)
printInOrder(root)