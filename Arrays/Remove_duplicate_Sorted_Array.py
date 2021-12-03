# Uisng Two pointers
#Remove duplicate from sorted array in place and return the length
arr = [1,2,2,3,3,3,4,4]

def remove_duplicates_sorted_array(arr):
    #left pointer pointing to a new poistion thats unique
    left = 1
    #right pointer to iterate the array
    for right in range(1,len(arr)):
        #compare current with previous if not equal replace left with right value 
        if arr[right] != arr[right-1]:
            arr[left] = arr[right]
        #Increase the left pointer    
            left+=1

    #Return length     
    return left 
    
remove_duplicates_sorted_array(arr)    