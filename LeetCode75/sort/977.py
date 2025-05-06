class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = []
        for i in nums:
            squared.append(i*i)
        return self.down(squared)
        
    def down(self, nums:List[int])-> List[int]:
        if len(nums)<2:
            return nums
        pivot = nums[-1]
        left = []
        right = []
        for j in nums[:-1]:
            if j<pivot:
                left.append(j)
            else:
                right.append(j)
        return self.down(left)+[pivot]+self.down(right)
