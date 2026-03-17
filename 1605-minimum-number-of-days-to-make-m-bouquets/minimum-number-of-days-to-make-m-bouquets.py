class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if(m*k>len(bloomDay)):
            return -1

        l=0
        r=max(bloomDay)

        while(l<=r):
            mid=(l+r)//2
            b=0
            f=0

            for day in bloomDay:
                if day<=mid:
                    f+=1

                    if f==k:
                        b+=1
                        f=0
                    
                else:
                    f=0

            if(b>=m):
                r=mid-1
            
            else:
                l=mid+1
        
        return l
