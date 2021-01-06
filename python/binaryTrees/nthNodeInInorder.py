#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None

index = [0] 
def nthNode(root,n):
    if root is not None:
        if index[0]<=n:
            nthNode(root.left,n)

            index[0] = index[0] + 1
            print(index[0])

            if index[0]==n:
                print("nth Node in Inroder traversaln is " + str(root.info))

            nthNode(root.right,n)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

nthNode(root,10)