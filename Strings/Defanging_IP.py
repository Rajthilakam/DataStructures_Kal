arr = "255.80.1.1"

def defang_ip(arr):
    res = ''
    a = (len(arr))
    for i in range(a):
        if arr[i] != '.':
            res += arr[i]
        else:
            res += '[.]'

    print(res)
    return res

defang_ip(arr)