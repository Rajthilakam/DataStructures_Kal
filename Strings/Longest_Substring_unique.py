def longestSubstringUnique(s):
        charSet = set()
        left=0
        right=0
        size=0
        n = len(s)
        
        for right in range(n):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            size = max(size,right-left+1)
        print(size)    
        return size
        
longestSubstringUnique('bcabc')  