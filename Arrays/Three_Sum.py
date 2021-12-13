#Return three elements that adds upto zero

def threeSum(nums):
    res = []
    nums.sort()
    # we need min 2 elements in the end so that it makes to total of three
    for i in range(len(nums)-2):
        #Checking current with previous if its same continue
        if i > 0 and nums[i] == nums[i-1]:
            continue
        #Declaring left and right pointers
        l, r = i+1, len(nums)-1
        #Iterate till left is less than right
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            #Increase left pointer if its less than zero
            if s < 0:
                l +=1 
            #Decrease the right pointer if its greater than zero    
            elif s > 0:
                r -= 1
            #If its equal to zero append to res    
            else:
                res.append((nums[i], nums[l], nums[r]))

                #check if left and next to it equal or not
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    print(res)            
    return res
    
nums = [1,-1,0,2,1,-2]
threeSum(nums)