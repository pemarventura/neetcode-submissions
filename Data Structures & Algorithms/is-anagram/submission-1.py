class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        ds = dict()
        dt = dict()

        for n in range(0, len(s)):
            if s[n] not in ds:
                ds[s[n]] = 1
            else:
                ds[s[n]] += 1

            if t[n] not in dt:
                dt[t[n]] = 1
            else:
                dt[t[n]] += 1
  
        return ds == dt
            
            
        