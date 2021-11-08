def find_rotate(str1,str2):
    if(len(str1) != len(str2)):
        return False
        
    clockwise_rot = ''
    anti_clockwise_rot = ''
        
    anti_clockwise_rot = str1[2:]+str1[0:2]
    clockwise_rot = str1[-2]+str1[:4]
    
    #return (str2 == clockwise_rot or str2 == anti_clockwise_rot)
    if (str2 == clockwise_rot or str2 == anti_clockwise_rot):
        return True
    else:
        return False    
    
find_rotate('amazon','onamaz')    