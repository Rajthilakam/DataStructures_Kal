arr = [2,4,6,7,8,9]
target = 10

def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    isAsc = arr[start] < arr[end]  
   
    while (start <= end):

        mid = int(start+(end-start)/2)

        if (target == arr[mid]):
            return mid

        if isAsc:
            if (target > arr[mid]):
                start = mid +1
            else:
                end = mid -1
        else:
            if (target > arr[mid]):
                end = mid - 1
            else:
                end = start + 1       
    return -1

binary_search(arr,target)                


