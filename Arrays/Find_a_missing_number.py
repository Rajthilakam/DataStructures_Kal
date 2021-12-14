arr = [1,2,2,3,4,7,8,6]

def find_missing_number(arr):
    n = len(arr)
    for i in range (n):
        #Taking index and reduced by one as array is zero index
        temp = abs(arr[i])-1
        if arr[temp] > 0:
            #Changing the values as visited in the corresponding index
            arr[temp]=arr[temp]*-1

    res = []

    for i,n in enumerate(arr):
        if (n > 0):
            res.append(i+1)
    print(res)        
    return res

find_missing_number(arr)