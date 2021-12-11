#Bottom Up Approach 
def Longest_Subseq(str1,str2):
    m = len(str1)
    n = len(str2)
    maxLength = 0

    dp = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])

            if dp[i][j] > maxLength:
                maxLength = dp[i][j]    

    print(maxLength)
    return maxLength

str1 = 'zxvio'
str2 = 'zcvm'

Longest_Subseq(str1,str2)