#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def leftBoundary(root,leftSum):
    if root.left is not None:
        root=root.left
        leftSum = root.info + leftBoundary(root,leftSum)
    elif root.right is not None:
        root=root.right
        leftSum = root.info + leftBoundary(root,leftSum)

    return leftSum

def rightBoundary(root,rightSum):
    if root.right is not None:
        root=root.right
        rightSum = root.info + leftBoundary(root,rightSum)
    elif root.left is not None:
        root=root.left
        rightSum = root.info + leftBoundary(root,rightSum)

    return rightSum

def totalSumFunc(root):
    if root is not None:
        val = root.info
        lSum = totalSumFunc(root.left)
        rSum =totalSumFunc(root.right)
        return val + lSum + rSum
    else:
        return 0


root = Node(8) 
root.left = Node(3) 

root.left.left = Node(1) 
root.left.right = Node(6) 
root.left.right.left = Node(4) 
root.left.right.right = Node(7) 

root.right = Node(10) 
root.right.right = Node(14) 
root.right.right.left = Node(13) 

leftSum =0
rightSum = 0
totalSum=0
uncoveredSum = root.info + leftBoundary(root,leftSum) + rightBoundary(root,rightSum)
coveredSum = totalSumFunc(root) - uncoveredSum
print(uncoveredSum)
if coveredSum == uncoveredSum:
    print("TRUE")
else:
    print("FALSE")