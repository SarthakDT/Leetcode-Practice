class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_s = [''.join(sorted(s)) for s in strs]

        hmap = {}

        for i in range(len(strs_s)):
            key=strs_s[i]

            if key not in hmap:
                hmap[key]=[]
        
            hmap[key].append(strs[i])

        return list(hmap.values())       