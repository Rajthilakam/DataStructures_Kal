from collections import OrderedDict 
arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]

def print_elements(arr):

    dict = OrderedDict()
    
    for num in arr:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num]+=1
            
    arr.sort(key=lambda x: (-dict[x], x))
    print (arr)
    return arr


print_elements(arr)