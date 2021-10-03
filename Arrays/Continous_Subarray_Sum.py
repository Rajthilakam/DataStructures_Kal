#Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.
#Examples :

#Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33

#Ouptut: Sum found between indexes 2 and 4

def subarray_givensum(arr,sum,n):

    if (n <= 0):
        print ("No elements in the array")
        return 

    curr_sum = 0
    start = 0
    end = 0

    while(end <= n):
        curr_sum+=arr[end]
        
       
        if (curr_sum == sum):
            print ("Sum found between index",start,end)
            return

        while (curr_sum > sum and start <= end):
            curr_sum-=arr[start]  
            start+=1

            if (curr_sum == sum):
                print ("Sum found between index",start,end)
                return

        end+=1


arr = [1,4,21,3,9,5]
n  = len(arr)
sum = 33
subarray_givensum(arr,sum,n)