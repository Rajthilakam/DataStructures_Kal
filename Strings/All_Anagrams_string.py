#Sliding Window 2 pointer approach

def solution(s1,s2):
    freq1 = [0]*26
    freq2 = [0]*26
    s1_len = len(s1)
    s2_len = len(s2)
    res = []
    
    for i in range(len(s1)):
        freq1[ord(s1[i])-ord('a')]+=1
        freq2[ord(s2[i])-ord('a')]+=1
    
    left = 0
    while(s1_len <= s2_len):
        if freq1 == freq2:
            res.append(left)
            
        
        if(s1_len != s2_len):
            freq2[ord(s2[s1_len])-ord('a')]+=1
        freq2[ord(s2[left])-ord('a')]-=1
        left+=1
        s1_len+=1
    print(res)    
    return res    
        
            
    
s1 = 'abc'
s2 = 'cbadeabc'
solution(s1,s2)