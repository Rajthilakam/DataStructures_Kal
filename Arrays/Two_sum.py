#Using Two Pointer technique Time Complexity 0(n) Space complexity o(1)

a = [-3,2,3,3,6,8,15]

target = 7

def two_sum(a,target):
    
    #Two Pointers one pointing to the start of the array and other at the end
    start = 0
    end = len(a)-1
    
    #Loop till start is less than end
    while start < end:
        sum = a[start] + a[end]
        if (sum == target):
            print ("The indices are",[start+1,end+1])
            return ([start+1,end+1])
            
        #Increase start by one if sum is less then target   
        elif (sum < target):
            start+=1
        
        #Decrease end by one if sum is greater than target    
        else:
            end = end-1

    print("There are no values with corresponding target")
    return None        
    
    
two_sum(a,target)        
