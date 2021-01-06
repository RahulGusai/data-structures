#! /usr/bin/python3


class Node(object):
    def __init__(self,value):
        self.left = None
        self.right = None
        self.info = value

    
def storeVertical(root,hd,m):
    if root is not None:
        try:
            m[hd].append(root.info)    
        except:
            m[hd] = [root.info]

        storeVertical(root.left,hd-1,m)
        storeVertical(root.right,hd=1,m)

    else:
        return  


def printVertical(m):
    for i in sorted(m):
        for val in m[i]:
            print(val,endline=" ")
        print()    


if __name__ == "__main__":
    root = Node(1) 
    
    root.left = Node(2)
    root.right = Node(3)
    
    root.left.left = Node(4)
    root.left.right = Node(2)

    root.right = Node(3)
    

    hd=0
    m = dict()
    storeVertical(root,hd,m)
