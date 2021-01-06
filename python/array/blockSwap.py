#! /usr/bin/python3



def blockSwap(arr,n,d):
    if n%d == 0:
        return arr
    else:
        temp = arr[0:d]
        index = 0
        for i in range(d,n):
            arr[index]=arr[i]
            index += 1

        for i in range(0,len(temp)):
            arr[index] = temp[i]
            index += 1

        return arr





arr = [1,2,3,4,5,6,7]

print("Before Swap = " + str(arr))
arr = blockSwap(arr,len(arr),2)
print(("After Swap = " + str(arr)))







