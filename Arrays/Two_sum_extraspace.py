#Time Complexity 0(n) Space complexity o(n)


a = [-3,2,3,3,6,8,15]

target = 6


def two_sum_hash(a,target):
    hashed = {}
    for i,n in enumerate(a):
        diff = target - n
        if diff in hashed:
            print([hashed[diff]+1,i+1])
            #Return the index which is one based
            return ([hashed[diff],i])
        hashed[n] = i    


two_sum_hash(a,target)