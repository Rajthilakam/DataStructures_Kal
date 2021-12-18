#Find the minimum jump required to reach the end of the array.Each array indices represents how many steps we can take
#IDeserve 
#Time complexity o(n)

arr = [1,4,3,7,1]

def jump(arr):
    ladder = arr[0]
    steps = arr[0]
    jump = 1
    
    if (len(arr) < 1):
        return 0
        
    for i in range(1,len(arr)):
        if (i == len(arr)-1):
           print(jump) 
           return jump
        # Calculate maxvalue for each index by adding index with corresponding value in the index       
        maxvalue = i+arr[i]
        
        # Ladder holds the max value 
        if (maxvalue > ladder):
            ladder = maxvalue
        
        # Reduce the steps by one
        steps-=1
        
        #If steps is zero increase the jump and calculate the value of step by subracting index from ladder
        if(steps == 0):
            jump+=1
            steps = ladder-i
    print(jump)        
    return jump        
        
        
jump(arr)     