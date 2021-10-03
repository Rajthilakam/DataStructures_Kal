#Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. 
# For example, in an array A:
#Example :
#Input : A[] = {-7, 1, 5, 2, -4, 3, 0}
#Output : 3
#3 is an equilibrium index, because:
#A[0] + A[1] + A[2]  =  A[4] + A[5] + A[6]
#Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n, returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.

#Time complexity o(n)

def equilibrium_index(arr,n):
    total_sum = 0
    left_sum = 0
    
    for i in range(n):
        total_sum+=arr[i]
        
    for i in range(n):
        total_sum -=arr[i]
        
        if (left_sum == total_sum):
            print ("Equilibrium index",i)
            return i
            
        left_sum+=arr[i]
        
    return -1    

arr = [ -7, 1, 5, 2, -4, 3, 0 ]
n = len(arr)
equilibrium_index(arr, n)