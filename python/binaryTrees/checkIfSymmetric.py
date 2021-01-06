#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def checkIfSymmetric(root):
    queue = []
    queue.append(root)

    while len(queue)>0:
        queueLen = len(queue)
        for i in range(0,queueLen):
            node = queue.pop(0)
            if node.left!=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)

        for i in range(0,int(len(queue)/2)):

            if queue[i].info == queue[len(queue)-i-1].info:
                pass
            else:
                print("NOT SYMMETRIC")    
                return

    print("SYMMETRIC")

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.right  = Node(3)
root.right.right = Node(3)

checkIfSymmetric(root)