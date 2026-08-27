class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        enc = set()
        l=0
        res=0

        for r in range(len(s)):
            while s[r] in enc:
                enc.remove(s[l])
                l+=1
            enc.add(s[r])
            res = max(res,r-l+1)
        
        return res