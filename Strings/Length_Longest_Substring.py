
def LCS(X, Y, m, n):
 
    maxLength = 0           
    endingIndex = m         
     
    lookup = [[0 for x in range(n + 1)] for y in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1): 
            
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
                 
                if lookup[i][j] > maxLength:
                    maxLength = lookup[i][j]
                    endingIndex = i

    return maxLength
    #return X[endingIndex - maxLength: endingIndex]
  
X = 'ABCD'
Y = 'BABA'

m = len(X)
n = len(Y)

print('The length of longest common substring is', LCS(X, Y, m, n))
 