#! /usr/bin/python3


def reArrange(arr):
    dictObj = {}
    for i in range(0,len(arr)):
        if i in dictObj.keys():
            if dictObj[i]>=i:
                dictObj[dictObj[i]]=arr[dictObj[i]]    
            arr[dictObj[i]]=i
            dictObj.pop(i,None)
        else:
            if arr[i]>=i:
                dictObj[arr[i]]=arr[arr[i]]
            arr[arr[i]]=i

    return arr

# arr = [2, 0, 1, 4, 5, 3]
# arr = [3, 2, 1, 0]
arr = [1, 3, 0, 2] 
arr = reArrange(arr)
print(arr)