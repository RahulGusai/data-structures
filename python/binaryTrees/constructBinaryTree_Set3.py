    #! /usr/bin/python3



class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def constructBinaryTree(preOrder,postOrder):
    if len(preOrder)==1:
        return Node(preOrder[0])   
    
    root = Node(preOrder[0])
    
    for i in range(0,len(postOrder)):
        if postOrder[i]==preOrder[1]:
            break

    root.left = constructBinaryTree(preOrder[1:i+2],postOrder[0:i+1])
    root.right = constructBinaryTree(preOrder[i+2:len(preOrder)],postOrder[i+1:len(postOrder)-1])

    return root    


def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print(root.info)
        printInOrder(root.right)


preOrder =  [1, 2, 4, 8, 9, 5, 3, 6, 7] 
postOrder = [8, 9, 4, 5, 2, 6, 7, 3, 1]

root = constructBinaryTree(preOrder,postOrder)
printInOrder(root)