#! /usr/bin/python3

class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None



def boundaryTraversal(root):
    leftBoundary = []
    temp = root.left
    while(temp!=None):
        leftBoundary.append(temp)
    
    temp = root.right
    rightBoundary = []
    while(temp!=None):
        rightBoundary.append(temp)
     