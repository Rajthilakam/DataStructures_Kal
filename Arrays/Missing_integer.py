#You are given a list of n-1 integers and these integers are in the range of 1 to n. 
# There are no duplicates in list. One of the integers is missing in the list. 
# Write an efficient code to find the missing integer.


#Time complexity o(n) space complexity o(1)
def missing_num(arr):
    n = len(arr)+1
    current_sum = 0
    expected_sum = round(n*(n+1)/2)
    for each in arr:
        current_sum+=each
    print (expected_sum - current_sum)    
    return expected_sum - current_sum    



arr = [1,4,3,5,6]
missing_num(arr)    