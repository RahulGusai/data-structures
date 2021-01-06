#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    ret = checkForSwap(arr)
    if ret==True:
        return 
    else:
        ret = checkForReverse(arr)
        if ret==True:
            return
        else:
            print("no")
            return

def func(x):
    return x

def checkForSwap(arr):
    n=len(arr)
    sortedArr = sorted(arr)
    swapIndexArr = []
    count = 0
    index = 0

    while( index<n ):
        if( arr[index]==sortedArr[index] ):
            index = index + 1
            continue
        else:
            swapIndexArr.append(index + 1)
            index = index + 1
            count = count + 1
            if( count>2 ):
                return False
    if count==0:
        print("yes")
        return True
    else:
        print("yes")
        print( "swap" + " " + str(swapIndexArr[0]) + " " + str(swapIndexArr[1]) )
        return True

def checkForReverse(arr):
    n=len(arr)
    sortedArr = sorted(arr)
    index = 0
    revIndexArray = []
    revFlag = False

    while( index<n ):
        val = arr[index]
        if ( val == sortedArr[index]):
            index = index + 1
            continue

        elif (revFlag==True):
            print("debug")
            return False
        
        else:
            print(val)
            ret = setRevStr(arr,index,val)
            if (ret==True):
                revIndexArray.append( index + 1 )
                revIndexArray.append( sortedArr.index(val) + 1 )
                index = index + ( sortedArr.index(val) - index ) + 1
                revFlag=True
            else:
                return False

    print("yes")
    print( "reverse" + " " + str(revIndexArray[0]) + " " + str(revIndexArray[1]) )
    return True

def setRevStr(arr,index,val):
    sortedArr = sorted(arr)
    j = sortedArr.index(val)

    while( index<=j ):
        if( sortedArr[j]==arr[index] ):
            index = index + 1
            j = j - 1
            continue
        else:
            return False

    return True

arr = [1,5,4,3,2,6]
ret = checkForReverse(arr)

print( ret )