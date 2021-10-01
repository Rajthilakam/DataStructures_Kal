#Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers 
# which has the largest sum.
#KadanaeAlgorithm
#Time complexity o(n) and Space Complexity o(1)
import sys
def subarray_largest_sum(arr):

    max_sum = -sys.maxsize-1
    curr_sum = 0

    for element in arr:
        curr_sum+=element

        if(curr_sum > max_sum):
            max_sum = curr_sum

        if (curr_sum < 0):
            curr_sum = 0

    print (max_sum)
    return max_sum            


arr = [-3,-3,-4,-6,-7]
subarray_largest_sum(arr)