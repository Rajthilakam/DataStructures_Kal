arr = [0,0,4,1,2,9]

def Longest_increase_subseq(arr):
    n = len(arr)
    lis = [0] * len(arr)
    print(lis)

    lis[0] = 1

    for i in range(1,len(arr)):
        for j in range(i):
            if (arr[i] > arr[j]) and  (lis[i] <= lis[j]):
                lis[i] = 1 + lis[j]

    print(lis)
    print(max(lis))
    return max(lis)

Longest_increase_subseq(arr)    