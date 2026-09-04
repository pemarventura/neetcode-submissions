class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls = []

        for n in range(0, len(nums)):
            if nums[n] in ls:
                return True
            
            ls.append(nums[n])
        
        return False

        