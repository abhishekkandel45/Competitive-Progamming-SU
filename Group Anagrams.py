class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        ans = []
        for i in d:
            ans.append(d[i])
        return ans
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """