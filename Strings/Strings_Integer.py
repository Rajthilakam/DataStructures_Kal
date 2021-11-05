def myAtoi(str):
        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = -2 ** 31    #-2147483648
        
        i = 0
        res = 0
        negative = 1
        
        
        while i < len(str) and str[i] == ' ':
            i += 1
                
        if i < len(str) and str[i] == '-':
            i += 1
            negative = -1
        elif i < len(str) and str[i] == '+':
            i += 1

        while (i < len(str) and str[i] >= '0' and str[i] <= '9'):
            if res > MAX_INT / 10 or (res == MAX_INT / 10 and int(str[i]) > 7):
                return MAX_INT if negative == 1 else MIN_INT

            res = res * 10  + (ord(str[i]) - ord('0')) 
            i+=1

        print(res*negative)
        return res * negative


myAtoi('-987')                   
