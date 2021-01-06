#! /usr/bin/python3


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def levelOrderTraversal(root):

    queue = []
    queue.append(root)

    while len(queue)>0:
        print(queue[0].data)

        node = queue[0]
        queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

levelOrderTraversal(root)