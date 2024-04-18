# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Solution
# Time complexity - O(n)
# Space complexity - O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [i,dic[target-nums[i]]]
            else:
                dic[nums[i]]=i

