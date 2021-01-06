#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def ternaryToTree(ternary,i):
    if i>=len(ternary):
        return None

    root = Node(ternary[i])
    i += 1

    if ( i<len(ternary) ) and ternary[i]=='?':
        root.left = ternaryToTree(ternary,i+1)

    elif i<len(ternary):
        root.right = ternaryToTree(ternary,i+1)

    return root

def printInOrder(root):
    if root is not None:
        print(root.info)
        printInOrder(root.left)
        printInOrder(root.right)

ternary = "a?b?c:d:e"
i=0
root = ternaryToTree(ternary,i) 
# printInOrder(root)
print(root.info)
print(root.left.info)
print(root.left.left.info)
print(root.left.left.right.info)
print(root.left.left.right.right.info)