class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroP = 0
        intP = 0
        if len(nums) == 1:
            print("break")
        else :
            while intP < len(nums) and zeroP < len(nums)-1:
                while zeroP < len(nums) and (nums[zeroP] is not 0) and (zeroP < intP):
                    zeroP += 1
                if nums[intP] is not 0:
                    temp = nums[intP] 
                    nums[intP] = nums[zeroP]
                    nums[zeroP] = temp
                intP += 1