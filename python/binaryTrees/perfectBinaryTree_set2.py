#! /usr/bin/python3



class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None



def printPerfectBinaryTreeReverse(root):
    queue = []
    stack = []

    queue.append(root)

    while len(queue)>0:
        if len(queue)==1:
            node = queue.pop(0)
            queue.append(node.left)
            queue.append(node.right)
            stack.append(node.right)
            stack.append(node.left)

        else:
            node1 = queue.pop(0)
            node2 = queue.pop(0)

            if node1.left is not None:
                queue.append(node1.right)
                queue.append(node2.left)
                queue.append(node1.left)
                queue.append(node2.right)

                stack.append(node2.left)
                stack.append(node1.right)
                stack.append(node2.right)
                stack.append(node1.left)

    while len(stack)>0:
        print(stack.pop(len(stack)-1).info,end = " ")


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
root.left.left.left.left = Node(16) 
root.left.left.left.right = Node(17) 
root.left.left.right.left = Node(18) 
root.left.left.right.right = Node(19) 
root.left.right.left.left = Node(20) 
root.left.right.left.right = Node(21) 
root.left.right.right.left = Node(22) 
root.left.right.right.right = Node(23) 
root.right.left.left.left = Node(24) 
root.right.left.left.right = Node(25) 
root.right.left.right.left = Node(26) 
root.right.left.right.right = Node(27) 
root.right.right.left.left = Node(28) 
root.right.right.left.right = Node(29) 
root.right.right.right.left = Node(30) 
root.right.right.right.right = Node(31)









printPerfectBinaryTreeReverse(root)