#! /usr/bin/python3



class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None




def constructSpecialTree(inOrder,sortedInOrder):
    if len(sortedInOrder)==0:
        return None

    elif len(sortedInOrder)==1:
        return Node(inOrder[0])
    
    else:
        root = Node(sortedInOrder[-1])

        for i in range(0,len(inOrder)):
            if inOrder[i]==sortedInOrder[-1]:
                break

        root.left = constructSpecialTree(inOrder[0:i],sortedInOrder[0:i])  
        root.right = constructSpecialTree(inOrder[i+1:len(inOrder)] , sortedInOrder[i:len(sortedInOrder)-1])

        return root


def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print(root.info)
        printInOrder(root.right)

inOrder = [1, 5, 10, 40, 30, 15, 28, 20]
root = constructSpecialTree(inOrder,sorted(inOrder))
printInOrder(root)







