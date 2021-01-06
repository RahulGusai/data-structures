#! /usr/bin/python3

def findSecondLargest(arr):
    l = arr[0]
    sl = arr[0]
    
    for i in range(0,len(arr)):
        if arr[i]>l:
            l = arr[i]
        else:
            if sl==l:
                sl=arr[i]
            elif (arr[i]>sl) and (arr[i]<l):
                sl = arr[i]

    if sl==l:
        return None
    else:
        return sl


# arr = [12, 35, 1, 10, 34, 1]
# arr = [10,34,5,10]
arr = [10,10,10]
number = findSecondLargest(arr)

if not number:
    print("No second largest element found")
else:
    print("Second largets number is- " + str(number))