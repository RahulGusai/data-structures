def removeDuplicates(nums):
    hashMap = {}
    for i in range(0,len(nums)):
        if nums[i] in list(hashMap.keys()):
            hashMap[nums[i]] = hashMap[i] + 1
        else:
            hashMap[nums[i]] = 0

    print(hashMap.keys())            
    return len(list(hashMap.keys()))


print(removeDuplicates([1,1,2]))