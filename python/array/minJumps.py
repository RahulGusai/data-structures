#! /usr/bin/python3


def minJumps(arr):
    length = len(arr)
    index = 0
    jump=0

    while(index<len(arr)):
        if arr[index]>=length-index-1:
            jump += 1
            break

        else:
            index = index+arr[index]
            jump += 1

    return jump


# arr = [1,3,5,8,9,2,6,7,6,8,9]
# arr = [1,1,1,1,1,1,1,1,1,1,1]
arr = [1,3,6,1,0,9]
number = minJumps(arr)
print(number)