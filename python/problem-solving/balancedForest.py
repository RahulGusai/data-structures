#!/bin/python3

import math
import os
import random
import re
import sys 
  
# the setrecursionlimit function is 
# used to modify the default recursion 
# limit set by python. Using this,  
# we can increase the recursion limit 
# to satisfy our needs 
  
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self,data):
        self.data=data
        self.child = []

def calculateSum(node):
    if node is not None:
        temp = node.data
        if len(node.child) != 0:
            for i in range(0,len(node.child)):
                temp = temp + calculateSum(node.child[i])
        return temp        

# Complete the balancedForest function below.
def balancedForest(c, edges):
    totalSum=0
    nodes = []
    for val in c:
        nodes.append(Node(val))
        totalSum = totalSum + val

    for e in edges:
        nodes[e[0]-1].child.append(nodes[e[1]-1])        

    resultArray = []    
    for i in range(0,len(edges)):
        for j in range(i+1,len(edges)):
            a=edges[i][1]
            b=edges[j][1]
            s1 = calculateSum(nodes[a-1])
            s2 = calculateSum(nodes[b-1]) 
            s3 = totalSum - s1 - s2
            
            # print("*******")
            # print('s1 = ' + str(s1))
            # print('s2 = ' + str(s2))
            # print('s3 = ' + str(s3))
            # print("*******")

            if (s1==s2==s3):
                resultArray.append(0)
            elif (s1==s2) and (s3<s1):
                resultArray.append(s1-s3)
            elif (s2==s3) and (s1<s2):
                resultArray.append(s2-s1)
            elif (s1==s3) and (s2<s1):
                resultArray.append(s1-s2)
       
    # print(totalSum)            
    # print(resultArray)            
    if len(resultArray)==0:
        return -1
    else:
        return min(resultArray)
                
if __name__ == '__main__':
    fptr = open("demo.txt", 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
