#Write a program to sort an array of 0's,1's and 2's in ascending order.
#Time complexity o(n)
#Dutch flag algorithm


def sort_zero_ones(arr):
    high=len(arr)-1
    mid = 0
    low = 0
    while (mid <= high):
        if(arr[mid] == 0):
            arr[low],arr[mid]=arr[mid],arr[low]
            mid = mid +1
            low = low+1
        elif(arr[mid] == 1):
            mid = mid +1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high = high-1
    print(arr)        
    return arr
    
arr = [2,1,0,0,1,2]    
sort_zero_ones(arr) 