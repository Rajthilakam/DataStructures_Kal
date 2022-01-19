def product(arr):
    n = len(arr)
    output = [1] * len(arr)
    output[0] = 1

    for i in range(1, n):
        output[i] = arr[i-1] * output[i-1]

    r = 1
    for i in range(n-1, -1, -1):
        output[i] = output[i] * r
        r = arr[i] * r

    return output


arr = [1, 2, 3, 4]
product(arr)
