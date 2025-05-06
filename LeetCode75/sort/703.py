class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = [-10001]
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.up(len(self.nums)-1)
        while len(self.nums) > self.k+1:
            self.nums[1] = self.nums.pop()
            self.down(1)
        return self.nums[1]

    def up(self, i:int):
        if self.nums[i] < self.nums[i//2]:
            self.nums[i], self.nums[i//2] = self.nums[i//2], self.nums[i]
        if  i != 0:
            return self.up(i//2)
    
    def down(self, i: int):
        left = i * 2
        right = i * 2 + 1

        if left < len(self.nums) and self.nums[left] < self.nums[smallest]:
            self.nums[i], self.nums[left] = self.nums[left], self.nums[i]
            return self.down(left)

        if right < len(self.nums) and self.nums[right] < self.nums[smallest]:
            self.nums[i], self.nums[right] = self.nums[right], self.nums[i]
            return self.down(right)