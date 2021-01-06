def trap(height):
    val=height[0]
    netCount=0
    for i in range(0,len(height)):
        if height[i]<val:
            count=0
            flag=None
            for j in range(i,len(height)):
                if height[j]<val:
                    count  = count + (val-height[j])
                else:
                    flag=1
                    break
            if flag!=None:
                netCount += count
                print(count)
                print(netCount)
                print("======")
                val=height[i]
                i = j + 1
                
            
        else:
            val=height[i]
        
    return netCount
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))