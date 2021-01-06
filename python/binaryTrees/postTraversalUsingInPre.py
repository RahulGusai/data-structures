#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def postOrderTraversal(inOrder,preOrder):
    if len(inOrder)!=0:
        if len(inOrder)==1:
            print(inOrder[0])
        else:
            i = inOrder.index(preOrder[0])
            postOrderTraversal(inOrder[0:i],preOrder[1:i+i])            
            postOrderTraversal(inOrder[i+1:len(inOrder)],preOrder[i+1:len(preOrder)])
            print(preOrder[0])



inOrder =  [4, 2, 5, 1, 3, 6]
preOrder = [1, 2, 4, 5, 3, 6]
postOrderTraversal(inOrder,preOrder)

