arr = [100,80,60,70,60,75,85]

def stock_span(arr):
    result = [1] * len(arr)

    if not arr:
        return

    s = []
    count = 1
    for i in reversed(range(len(arr))):
        while s and arr[i] < arr[s[-1]]:
            count+=1
        result[s[-1]] = count
        count = 1
        s.pop()

        s.append(i)    
    print(result)
    return result

stock_span(arr)   