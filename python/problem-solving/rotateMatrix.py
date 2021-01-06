#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    rows = len(matrix)
    columns = len(matrix[0])
    ret = False
    count = 0
    n = 0

    while( n<rows): 
        if( ret==False):
            rotations = (columns - n*2)*2 + (rows - 2 - 2*n)*2
            rotations = (r%rotations)
            while( count<rotations ):
                ret = rotateMatrix(n,rows,columns)
                count = count + 1
            count = 0    
            n = n + 1 
        else:
            break        
        
    printMatrix()

def printMatrix():
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(0,rows):
        string = "" 
        for j in range(0,columns):
            string = string + "{0:d} ".format( (matrix[i])[j] ) 
        print(string)

def rotateMatrix(n,rows,columns):
    i = n
    j = n
    temp = (matrix[i])[j]
    flag = False

    while (i+1)<rows-n:
        i = i + 1
        if (i==n+1) and (j==n+1):
            flag = True
        swap = (matrix[i])[j] 
        (matrix[i])[j] = temp
        temp = swap
            
    while (j+1)<columns-n:
        j = j + 1
        if (i==n+1) and (j==n+1):
            flag = True
        swap = (matrix[i])[j] 
        (matrix[i])[j] = temp
        temp = swap

    while (i-1)>=n:
        i = i - 1
        if (i==n+1) and (j==n+1):
            flag = True
        swap = (matrix[i])[j] 
        (matrix[i])[j] = temp
        temp = swap

    while (j-1)>=n:
        j = j - 1
        if (i==n+1) and (j==n+1):
            flag = True
        swap = (matrix[i])[j] 
        (matrix[i])[j] = temp
        temp = swap

    return flag     


if __name__ == '__main__':

    matrix = [ [1, 2, 3, 4],[7, 8, 9, 10],[13, 14, 15, 16],[19, 20, 21, 22],[25, 26, 27, 28] ]
    r = 1

    matrixRotation(matrix, r)
    print(matrix)