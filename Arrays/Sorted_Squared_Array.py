#Two pointers Time complexity o(n) Space complexity o(n)
#Sorted Square array

def sorted_square_array(arr, n):
    #Initalize left and right pointers to zero and length of the array
    left, right = 0, n - 1

    index = n - 1
    #Intialize a result with 0 of array length
    result = [0 for x in arr]
    

    while index >= 0:
        #Compare the value of first and last index if its greater assign to arr[left] and increase the pointer
        if abs(arr[left]) >= abs(arr[right]):
            result[index] = arr[left] * arr[left]
            left += 1
        else:
            result[index] = arr[right] * arr[right]
            right -= 1
        index -= 1

    print(result)
    return result 
   
# Driver code
arr = [-6, -3, -1, 2, 4, 5 ]
n = len(arr)

sorted_square_array(arr,n)