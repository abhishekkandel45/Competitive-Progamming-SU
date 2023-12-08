class Solution:
    def match(self, wild, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(wild) + 1)]
        
        dp[0][0] = True
        
        for i in range(1, len(pattern) + 1):
            if pattern[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]
        
        for i in range(1, len(wild) + 1):
            for j in range(1, len(pattern) + 1):
                if wild[i - 1] == pattern[j - 1] or wild[i - 1] == '?' or pattern[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif wild[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i - 1][j - 1]
        
        return dp[len(wild)][len(pattern)]

# Example usage:
s = Solution()
wild = "*c*d"
pattern = "abcd"
print(s.match(wild, pattern))  # Output: True
