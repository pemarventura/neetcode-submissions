class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for n in range(0, len(strs)):
            sort = "".join(sorted(strs[n]))
            if sort not in dic:
                dic[sort] = [strs[n]]
                continue
            
            dic[sort].append(strs[n])
        
        return list(dic.values())
            

        

        