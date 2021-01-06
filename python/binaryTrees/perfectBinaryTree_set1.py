#! /usr/bin/python3



class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None



def printPerfectBinaryTree(root):
    queue = []

    queue.append(root)

    while len(queue)>0:
        if len(queue)==1:
            node = queue.pop(0)
            print(node.info,end=" ")
            queue.append(node.left)
            queue.append(node.right)

        else:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            print(node1.info,end=" ")
            print(node2.info,end=" ")

            if node1.left is not None:
                queue.append(node1.left)
                queue.append(node2.right)

                queue.append(node1.right)
                queue.append(node2.left)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)                    
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

printPerfectBinaryTree(root)