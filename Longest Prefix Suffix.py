class Solution:
    def lps(self, s):
        n = len(s)
        lps = [0]*n
        i = 1
        j = 0
        while i < n:
            if s[i] == s[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps[-1]  # return the length of the longest prefix/suffix

