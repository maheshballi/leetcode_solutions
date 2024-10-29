from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       num_to_index = {}

       for index, number in enumerate(nums):
            required_number = target - number

            if required_number in num_to_index:
                return [num_to_index[required_number], index]
            num_to_index[number] = index


solution =Solution()
nums = [1, 3, 4, 56]
target = 7
print(solution.twoSum(nums, target))