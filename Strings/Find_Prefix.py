def longestCommonPrefix(strs):
        minlen = min([len(x) for x in strs])
        common_prefix=0
        
        for i in range(minlen):
            cont=1
            current = strs[0][i]
            
            for j in range(1,len(strs)):
                if strs[j][i]!=current:
                    cont=0
                    break
                
            if cont==0:
                break
            else: 
                common_prefix+=1
                
        result = strs[0][:common_prefix]
        if (len(result)):
            print("The longest common prefix is ",result)
        else:
            print("There is no common prefix")    
        return result 
        
strs = ['apple','ape','april']       
longestCommonPrefix(strs) 