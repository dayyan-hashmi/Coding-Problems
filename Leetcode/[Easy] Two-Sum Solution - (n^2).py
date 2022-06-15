class Solution: #My Solution w/Brute Force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        indices = []
        length = len(nums) - 1
        
        while (i < length):
            j = i + 1
            while (j <= length):
                if (nums[i] + nums[j] == target):
                    indices.append(i)
                    indices.append(j)
                    return indices
                else:
                    j = j + 1
            i = i + 1 
