
def house_robber(nums):
    if not nums: 
        return 0
    if len(nums) == 1: 
        return nums[0]
    
    dp = [0] * len(nums)

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
      dp[i] = max(nums[i] + dp[i-2], dp[i-1])

    print(dp[-1])  
    return dp[-1] # return the last element

nums = [1,2,3,4,5]    
house_robber(nums)
