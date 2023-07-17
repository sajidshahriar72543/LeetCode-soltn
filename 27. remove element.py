class Solution(object):
    def removeElement(self, nums, val):
        for i in range(len(nums)):
           if nums[i] == val:
            nums[i] = '_'
        while '_' in nums:
            nums.remove('_')
        return len(nums)