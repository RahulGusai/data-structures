#! /usr/bin/python3

## Both array are in the ascending order

def smallestPairs(arr1,arr2,k):
    i = 0 #arr1
    j = 0 #arr2
    pairs = []
    for _ in range(0,k):
        temp = []
        temp.append(arr1[i])
        temp.append(arr2[j])
        print(temp)

        if arr1[i]<arr2[j]:
            print("y")
            if j < len(arr2)-1:
                j += 1
            else:
                j = 0
                i += 1
        else:
            print("N")
            if i < len(arr1)-1:
                i += 1
            else:
                i = 0
                j += 1
        pairs.append(temp)

    return pairs

arr1 = [1,3,11]
arr2 = [2,4,8]
k=4

pairs = smallestPairs(arr1,arr2,k)
print(pairs)
