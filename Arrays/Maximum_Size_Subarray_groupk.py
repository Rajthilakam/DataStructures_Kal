#Sliding Window technique Time complexity o(n) space complexity o(1)

def maximum_subarray_groupk(arr,k):
    max_sum = 0
    window_sum = 0
    
    #Get sum for the first window
    for i in range(k):
        window_sum+=arr[i]

    #Assign the max_sum to current window sum    
    max_sum = window_sum

    #Initialize the start pointer to zero
    start = 0

    #Iteate from k to len(arr)
    for i in range(k,len(arr)):
        #Add the next array element and eliminate the previous one
        window_sum = window_sum + arr[i] - arr[start]

        #Increase the start pointer by one
        start+=1

        #Compare max_sum with window sum if lesser assign the value of window sum to max_sum
        if (max_sum < window_sum):
            max_sum = window_sum    
    print(max_sum)  
      
    #Return max_sum
    return max_sum    


arr = [3,2,5,4,1]        
k=2
maximum_subarray_groupk(arr,k)
