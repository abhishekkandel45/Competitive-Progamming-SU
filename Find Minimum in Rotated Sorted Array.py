class Solution (object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the index of the minimum element in the array
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]