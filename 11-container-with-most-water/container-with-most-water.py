class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_cap = 0
        while l<r:
            cap = (r-l)*min(height[l],height[r])
            max_cap = max(cap,max_cap)

            if height[l]<height[r]:
                l+=1
            elif height[r]<height[l]:
                r-=1
            else:
                l+=1
                r-=1
            
        return max_cap