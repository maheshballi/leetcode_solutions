from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n

 
solution = Solution()
nums = [1, 3, 4, 4, 5]
val = 4  # Specify the value to remove
new_length = solution.removeElement(nums, val)
print("New length after removal:", new_length)
print("Modified list:", nums[:new_length]) 