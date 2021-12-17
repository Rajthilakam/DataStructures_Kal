input = [2, 7, 3,9, 4, 6, 5]

def findgreaterleft(input):
    if not input:
        return 
    s = []
    result = [-1] * len(input)

    for i in reversed(range(len(input))):
        while s and input[i] > input[s[-1]]:
            result[s[-1]] = input[i]
            s.pop()
        #Storing the index in stack popping out once we find the value for the corresponding index   
        s.append(i)
    print(result)         
    return result    

findgreaterleft(input)