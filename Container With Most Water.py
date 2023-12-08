class Solution (object):
    def maxArea (self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        start = 0
        end = len (height) - 1
        while start < end:
            area = min (height[start], height[end]) * (end - start)
            max_area = max (max_area, area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area


# Driver Code
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
obj = Solution ()
print (obj.maxArea (height))
