class Solution:
    def countPS (self, string):
        # Code here
        n = len(string)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if string[i] == string[j]:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
        return dp[0][n-1] % (10**9 + 7)



#Driver Code
if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        str = input()
        ob=Solution()
        print(ob.countPS(str))
# } Driver Code Ends
