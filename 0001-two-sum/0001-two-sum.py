class Solution(object):
    nums = [2,7,11,15]
    target = 9
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return([i, j])
       
    
solution = Solution()
nums = [3,2,4]
target = 6
print(solution.twoSum(nums, target))