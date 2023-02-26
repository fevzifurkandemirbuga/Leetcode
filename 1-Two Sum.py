class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)-1):
            if not target-nums[i] in nums[i+1::]:
                continue
            
            return [i,nums.index(target-nums[i],i+1)]
