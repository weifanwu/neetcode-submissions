class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = nums[0]
        result = float('inf')
        left, right = 0, 0
        while right < len(nums):
            if currentSum >= target:
                result =min(result, right - left + 1)
                currentSum = currentSum - nums[left]
                left = left + 1
            else:
                right = right + 1
                if right < len(nums):
                    currentSum = currentSum + nums[right]
        return 0 if result == float('inf') else result