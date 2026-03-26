class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix =  strs[0]
        for j in range(1,len(strs)):
            i = 0
            while i < min(len(prefix),len(strs[j])) and prefix[i]==strs[j][i]:
                i+=1
            
            prefix = prefix[:i]
        
        if prefix == "":
            return ""

        return "".join(prefix)        