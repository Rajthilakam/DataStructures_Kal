#Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. 
# It is given that ll array elements are distinct.
# Time complexity worstcase o(n^2) average o(n)

def kthSmallest(arr,k):
    k = k - 1
      
    def quickselect(left_index,right_index):
        pivot_value = arr[right_index]
        pivot_index = left_index
        
        for i in range(left_index,right_index):
            if arr[i] <= pivot_value:
                arr[pivot_index],arr[i] = arr[i],arr[pivot_index]
                pivot_index+=1
                
        arr[pivot_index],arr[right_index] = arr[right_index],arr[pivot_index]        
        
        if(pivot_index > k):
            print(arr,'left index')
            return quickselect(left_index,pivot_index-1)
        elif(pivot_index < k):
            print(arr,'right index')
            return quickselect(pivot_index+1,right_index) 
        else:
            print(arr)
            return arr[pivot_index]
            
    return quickselect(0,len(arr)-1)
    
arr = [7, 10, 4, 3, 20, 15]

k = 4
print("K'th smallest element is",
           kthSmallest(arr,k))
            