#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def postOrderUsingTwoStacks(root):
    stack1 = []
    stack2 = []

    stack1.append(root)

    while len(stack1)>0:
        node = stack1.pop()
        stack2.append(node)

        if node.left is not None:
            stack1.append(node.left)

        if node.right is not None:
            stack1.append(node.right)

    while len(stack2)>0:
        print(stack2.pop().info,end=" ")



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)      

postOrderUsingTwoStacks(root)