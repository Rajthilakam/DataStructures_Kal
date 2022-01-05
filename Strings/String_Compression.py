#Time complexity o(n)
def string_compression(stri):
    result = ''
    index = 0
    str_length = len(stri)
    while index != str_length:
        count = 1
        while (index < str_length-1) and (stri[index] == stri[index+1]):
            count+=1
            index+=1

        if count == 1:
            result+=stri[index]
        else:
            result+=stri[index]+str(count)    
        index+=1
    print(result)    
    return result

string_compression('pppeedd')    