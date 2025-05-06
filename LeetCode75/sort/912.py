class Solution:
    def sortArray(self, nums:List[int]) -> List[int]:
        result = []
        self.nums = [-50001]
        for n in nums:
            self.add(n)
        while len(self.nums)>1:
            result.append(self.remove())
        return result  
    
    def add(self, n:int):
        self.nums.append(n)
        if len(self.nums) == 2:
            return# 루트 노드일시
        i = len(self.nums)-1 # 현재 위치
        
        while self.nums[i//2] > self.nums[i]:
            self.nums[i//2], self.nums[i] = self.nums[i], self.nums[i//2]
            i = i//2 

    def remove(self)->int:
        returnInt = self.nums[1]
        if len(self.nums) == 2:
            self.nums.pop()
            return returnInt
        self.nums[1] = self.nums.pop()
        self.down(1)
        return returnInt
        
    def down(self, i: int):
        left = i * 2
        right = i * 2 + 1
        smallest = i

        if left < len(self.nums) and self.nums[left] < self.nums[smallest]:
            smallest = left
        if right < len(self.nums) and self.nums[right] < self.nums[smallest]:
            smallest = right

        if smallest != i:
            self.nums[i], self.nums[smallest] = self.nums[smallest], self.nums[i]
            return self.down(smallest)