from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0  # Reset the count when encountering a zero

        return max_count
    
s = Solution()
# Example Test Cases
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # Output: 3
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))  # Output: 2