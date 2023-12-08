class Solution:
    def maxOfMin(self, arr,n):
        #code here
        # Find index of next smaller element for every element
        left = [-1]*n
        right = [n]*n
        s = []
        for i in range(n):
            while len(s) != 0 and arr[s[-1]] >= arr[i]:
                s.pop()
            if len(s) != 0:
                left[i] = s[-1]
            s.append(i)
        s.clear()
        for i in range(n-1, -1, -1):
            while len(s) != 0 and arr[s[-1]] >= arr[i]:
                s.pop()
            if len(s) != 0:
                right[i] = s[-1]
            s.append(i)
        ans = [0]*n
        for i in range(n):
            length = right[i] - left[i] - 1
            ans[length-1] = max(ans[length-1], arr[i])
        for i in range(n-2, -1, -1):
            ans[i] = max(ans[i], ans[i+1])
        return ans