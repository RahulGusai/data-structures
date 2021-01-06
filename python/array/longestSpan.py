#! /usr/bin/python3


def longestSpan(arr1,arr2):
    length = len(arr1)
    sum1 = [0 for i in range(length)]
    sum2 = [0 for i in range(length)]

    for i in range(1,length):
        sum1[i] = sum1[i-1] + arr1[i]           
        sum2[i] = sum2[i-1] + arr2[i]

    index = length
    while(index>0):
        for i in range(0,length-index+1):
            if sum(arr1[i:i+index])==sum(arr2[i:i+index]):
                return index
        index -= 1

    return 0


arr1 = [0,1,0,0,0,0]
arr2 = [1,0,1,0,0,1]
print( longestSpan(arr1,arr2) )
