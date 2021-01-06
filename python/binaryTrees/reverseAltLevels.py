#! /usr/bin/python3


class Node(object):
    def __init__(self,info):
        self.info=info
        self.left=None
        self.right=None


def reverseAltLevel(root):
    queue = []
    flag = True
    queue.append(root)

    while len(queue)>0:
        if flag==True:
            print("yess")
            print("length= " + str(len(queue)))
            for node in queue:
                print("val = " + str(node.info))


            if len(queue)==1:
                node = queue.pop(0)
                if node.left!=None:
                    queue.append(node.left)
                    queue.append(node.right)

                    ## Replace nodes
                    temp = node.right
                    node.right = node.left
                    node.left = temp

            else:
                tempQueue = queue
                noOfNodes = len(queue)
                for i in range(0,noOfNodes):
                    node = queue.pop(0)
                    if node.left!=None:
                        queue.append(node.left)
                        queue.append(node.right)

                for i in range(0,int(noOfNodes/2)):
                    node1 = tempQueue[i]
                    node2 = tempQueue[noOfNodes-i-1]
                    
                    if node1.left!=None:
                        print("DEBUGGGGGGGGGGG")
                        temp = node2.right
                        node2.right = node1.left
                        node1.left = temp      

                        if node1.left.left is not None:
                            temp = node1.left.left
                            node1.left.left = node2.right.left
                            node2.right.left = temp
                            
                            temp = node1.left.right
                            node1.left.right = node2.right.right
                            node2.right.right = temp

                        temp = node1.right
                        node1.right = node2.left
                        node2.left = temp        

                        if node1.right.left is not None:
                            temp = node1.right.left
                            node1.right.left = node2.left.left
                            node2.left.left = temp

                            temp = node1.right.right
                            node1.right.right = node2.left.right
                            node2.left.right = temp

            flag = False

        else:
            print("nooo")
            print("length= " + str(len(queue)))
            for node in queue:
                print("val = " + str(node.info))
            
            noOfNodes = len(queue) 
            i=0
            while i<noOfNodes:
                node = queue.pop(0)
        
                if node.left!=None:
                    queue.append(node.left)    
                    queue.append(node.right)
                
                i=i+1

            flag = True


def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.left)
        print(root.info)
        inOrderTraversal(root.right)

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


inOrderTraversal(root)
print("**********************")
reverseAltLevel(root)
print("**********************")
inOrderTraversal(root)