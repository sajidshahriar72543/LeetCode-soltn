from collections import OrderedDict
class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] =  OrderedDict.fromkeys(nums)
        return len(nums)
    
# why OrderedDict.fromkeys(nums) works but not set(nums)?
# Because: set(nums) will change the order of the list, but OrderedDict.fromkeys(nums) will not.