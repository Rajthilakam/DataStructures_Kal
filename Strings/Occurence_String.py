def strStr(str1, str2):
   
    if not str2:
        return 0
    str2_len = len(str2)
    for idx, val in enumerate(str1):
        if val != str2[0]:
            continue
        if str1[idx:idx+str2_len] == str2:
            print('The first occurence of the index of the string is',idx)
            return idx
    return -1
    
str1 = 'helol'
str2 = 'l'
strStr(str1,str2)