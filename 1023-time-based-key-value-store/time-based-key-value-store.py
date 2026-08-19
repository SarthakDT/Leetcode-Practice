class TimeMap(object):

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.store:
            return ""

        l = 0
        r = len(self.store[key])-1
        res = ""
        while l<=r:
            mid = (l+r)//2
            if self.store[key][mid][0]==timestamp:
                return self.store[key][mid][1]
            
            elif self.store[key][mid][0]>timestamp:
                r=mid-1
            else:
                l=mid+1
                res=self.store[key][mid][1]
        
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)