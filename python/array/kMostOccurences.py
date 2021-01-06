#! /usr/bin/python3


def kMostOccurences(arr,k):
    dictObj = {}
    for i in range(0,len(arr)):
        if arr[i] in dictObj.keys():
            dictObj[arr[i]] += 1
        else:
            dictObj[arr[i]] = 1

    numbers = []
    index = 0
    while index<k:
        maxVal = None
        maxValIndex = None
        for key,val in dictObj.items():
            if (maxVal==None) and (maxValIndex==None):
                maxVal = val
                maxValIndex = key
            elif val>maxVal:
                maxValIndex=key
                maxVal = val
            elif val==maxVal:
                if key>maxValIndex:
                    maxValIndex=key
                    maxVal = val
        
        numbers.append(maxValIndex)
        dictObj.pop(maxValIndex,None)
        index += 1
    
    return numbers

arr =  [3, 1, 4, 4, 5, 2, 6, 1]
k = 2
numbers = kMostOccurences(arr,k)
print(numbers)