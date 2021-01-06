#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None

def constructBinaryTree(preOrder,inOrder):
        if len(preOrder)==0:
            return None
        
        elif len(preOrder)==1:
            return Node(preOrder[0])

        else:
            root = Node(preOrder[0])

            for i in range(0,len(inOrder)):
                if preOrder[0]==inOrder[i]:
                    break

            root.left = constructBinaryTree(preOrder[1:i+1],inOrder[0:i])
            root.right = constructBinaryTree(preOrder[i+1:len(preOrder)],inOrder[i+1:len(inOrder)])
            
            return root

def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        printInOrder(root.right)    
        print(root.info)


# inOrder =  ['D', 'B' ,'E' ,'A' ,'F', 'C' ]
# preOrder = ['A','B','D','E','C','F']
# inOrder = [ 9, 8, 4, 2, 10, 5, 10, 1, 6, 3, 13, 12, 7 ] 
# preOrder = [ 1, 2, 4, 8, 9, 5, 10, 10, 3, 6, 7, 12, 13 ] 
# inOrder = [1, 2, 4, 5, 6 ,8 ,7]
# preOrder =[1, 2, 4, 5, 6, 7, 8]
inOrder = [3, 1, 4, 0 , 5, 2]
preOrder = [0, 1, 3, 4, 2, 5]

root = constructBinaryTree(preOrder,inOrder)

printInOrder(root)

