class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        biggest = sum(nums[0:k])
        mySum = sum(nums[0:k])
        for i in range(len(nums)-k):
            mySum += nums[k+i] - nums[i]
            if mySum > biggest:
                biggest = mySum
        return biggest/k