#! /usr/bin/python3



class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


index = [0]

def constructSpecialTree(preOrder,preLn):
    if index[0]==len(preOrder)-1: 
        return Node(preOrder[index[0]])
    
    elif preLn[index[0]]=='L':
        return Node(preOrder[index[0]])

    else:
        root = Node(preOrder[index[0]])
        index[0] += 1
        root.left = constructSpecialTree(preOrder,preLn)
        index[0] += 1
        root.right = constructSpecialTree(preOrder,preLn)
    
        return root

def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print(root.info)
        printInOrder(root.right)

preOrder = [10, 30, 20, 5, 15]
preLn = ['N', 'N', 'L', 'L', 'L']
root =constructSpecialTree(preOrder,preLn)
printInOrder(root)















