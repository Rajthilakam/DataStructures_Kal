#Time complexity 0(n^2) Space Complexity 0(1)

def expand(s, low, high):
    length = len(s) 
    # expand in both directions
    while low >= 0 and high < length and s[low] == s[high]:
        low = low - 1
        high = high + 1 
    # return palindromic substring
    return s[low + 1:high]
  
def findLongestPalindromicSubstring(s): 
    # base case
    if not s or not len(s):
        return ''
    max_str = ''
    max_length = 0
   
    for i in range(len(s)):
        
            curr_str = expand(s, i, i)
            curr_length = len(curr_str)
     
            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str
           
            curr_str = expand(s, i, i + 1)
            curr_length = len(curr_str)
      
            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str
 
    return max_str
  
s = 'babad'
 
print('The longest palindromic substring of is',
            findLongestPalindromicSubstring(s))   