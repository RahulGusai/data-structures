#! /usr/bin/python3


# Linked List node 
class ListNode: 
        # Constructor to create a new node 
        def __init__(self, data): 
            self.data = data 
            self.next = None
  
# Binary Tree Node structure 
class BinaryTreeNode: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


def pushToLL(head,val):
    newNode = ListNode(val)
    newNode.next = head
    head = newNode
    return newNode


def constructBinaryTree(head):
    queue = []
    root = BinaryTreeNode(head.data)
    queue.append(root)

    while True:
        node = queue.pop(0)

        if head.next is not None:
            head = head.next
            newNode = BinaryTreeNode(head.data)
            queue.append(newNode)
            node.left = newNode
        else:
            break

        if head.next is not None:
            head = head.next
            newNode = BinaryTreeNode(head.data)
            queue.append(newNode)
            node.right = newNode
        else:
            break

    return root        


def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print(root.data)
        printInOrder(root.right)



head = None
head = pushToLL(head,36)
head = pushToLL(head,30)
head = pushToLL(head,25)
head = pushToLL(head,15)
head = pushToLL(head,12)
head = pushToLL(head,10)


root = constructBinaryTree(head)
printInOrder(root)