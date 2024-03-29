class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l,r = l+1,r-1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res

# Driver Code
nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(nums))

