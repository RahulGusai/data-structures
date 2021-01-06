#!/bin/python3

import os
# importing the sys module 
import sys 
  
# the setrecursionlimit function is 
# used to modify the default recursion 
# limit set by python. Using this,  
# we can increase the recursion limit 
# to satisfy our needs 
  
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


#
# Complete the swapNodes function below.
#
def rotateByDepth(root,level):
    if root is not None:
        if(level==1):
            temp = root.left
            root.left = root.right
            root.right = temp
        else:
            rotateByDepth(root.left,level-1)
            rotateByDepth(root.right,level-1)

def fetchHeight(root):
    if root is None:
        return 0
    else:
        lHeight = fetchHeight(root.left)
        rHeight = fetchHeight(root.right)

        if(lHeight>rHeight):
            return lHeight+1
        else:
            return rHeight+1    

def inorderTraversal(root):
    if root is not None:
        inorderTraversal(root.left)
        arr.append(root.data)
        inorderTraversal(root.right)


def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    global arr
    nodes = []

    for i in range(1,len(indexes)+1):
        nodes.append(Node(i))

    for i in range(0,len(indexes)):
        a = indexes[i][0]
        b = indexes[i][1]
        
        if a==-1:
            nodes[i].left=None
        else:
            nodes[i].left = nodes[a-1]        

        if b==-1:
            nodes[i].right=None
        else:
            nodes[i].right=nodes[b-1]        
    
    hTree = fetchHeight(nodes[0])        
    resultArray = []
    for k in queries:
        multiplesArr = []
        elem = k
        index=1
        while(elem<=hTree):
            multiplesArr.append(elem)
            elem=elem
            index = index + 1
            elem = k*index
            
        for i in range(1,hTree+1):
            if i in multiplesArr:
                rotateByDepth(nodes[0],i)

        arr = []        
        inorderTraversal(nodes[0])            
        resultArray.append(arr)        

    return resultArray

if __name__ == '__main__':
    fptr = open("demo.txt", 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
