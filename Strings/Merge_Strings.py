str1 = 'abcd'
str2 = 'ef'

def solution(str1,str2):
    res = ''
    left = 0
    right = 0
    
    while (left < len(str1) or right < len(str2)):
        if (left < len(str1)):
            res+=str1[left]               
            left+=1
        if (right < len(str2)): 
            res+=str2[right]
            right+=1
    return res    
    
    
solution(str1,str2)    