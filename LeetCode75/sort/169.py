class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if nums[-1] == i:
                count += 1
        if len(nums)//2 < count :
            return nums[-1]
        else:
            return self.majorityElement(nums[:-1])
        