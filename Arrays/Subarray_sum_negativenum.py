#Given an unsorted array of integers, find a subarray which adds to a given number. 
# If there are more than one subarrays with sum as the given number, print any of them.

#nput: arr[] = {10, 2, -2, -20, 10}, sum = 20

#Ouptut: No subarray with given sum exists

#Time complexity o(n)

def subArraySum(arr, n, Sum):
     
    dict = {}
 
    curr_sum = 0
   
    for i in range(0,n):
      
        curr_sum += arr[i]
   
        if curr_sum == Sum:
            print("Sum found between indexes 0 to", i)
            return
          
        if (curr_sum - Sum) in dict:
          
            print("Sum found between indexes", \
                   dict[curr_sum - Sum] + 1, "to", i)           
            return
   
        dict[curr_sum] = i
   
    print("No subarray with given sum exists")


arr = [10, 2, -2, -20, 10]  
n=len(arr)
Sum = -10
subArraySum(arr, n, Sum)
