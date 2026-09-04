class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        
        for n in range(0, len(nums)):
            if nums[n] in d:
                return True
            else:
                d[nums[n]] = 1


        return False


        