class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """