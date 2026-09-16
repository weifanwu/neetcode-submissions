class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero = zero + 1
            elif nums[i] == 1:
                one = one + 1
            elif nums[i] == 2:
                two = two + 1
        
        for i in range(0, len(nums)):
            if zero != 0:
                nums[i] = 0
                zero = zero - 1
            elif one != 0:
                nums[i] = 1
                one = one - 1
            elif two != 0:
                nums[i] = 2
                two = two - 1