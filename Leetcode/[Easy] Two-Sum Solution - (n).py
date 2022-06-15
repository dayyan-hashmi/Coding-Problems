class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        hmap = {} #Dictionary / HMap
        for i, value in enumerate(nums):
            remainder = target - value
            if (remainder in hmap):
                return (i, hmap[remainder])
            hmap[value] = i
        
