class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)

        while l<=r:
            mid=(l+r)//2

            s=0
            count=1
            for w in weights:
                if s+w<=mid:
                    s+=w
                
                else:
                    s=w
                    count+=1
            
            if count<=days:
                r=mid-1

            else:
                l=mid+1
            
        return l