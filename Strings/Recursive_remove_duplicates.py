def str_remove(string1):
    res = string1
    temp = ''
    while (len(temp) != len(res)):
        temp = res
        res = remove_adj(res)
        
    return res
    
def remove_adj(s):
    
    i = 0
    n = len(s)
    res = ''
    while(i < n):
        if (i < n-1 and s[i] == s[i+1]):
            while (i < n-1 and s[i] == s[i+1]):
                i+=1
                
        else:
            res+=s[i]
        i+=1
    print(res)
    return res
        
str_remove('acaaabbbacdddd') 