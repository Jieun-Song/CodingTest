class Solution:
    def __init__(self):
        self.head = [0]
    def lastStoneWeight(self, stones: List[int]) -> int:
        for s in stones:
            self.head.append(s)
            self.up(len(self.head)-1)

        while len(self.head) > 2:
            self.head[1], self.head[-1] = self.head[-1],self.head[1]
            num1 = self.head.pop()
            self.down(1)

            self.head[1], self.head[-1] = self.head[-1],self.head[1]
            num2 = self.head.pop()
            self.down(1)

            if num1 > num2:
                self.head.append(num1-num2)
                self.up(len(self.head)-1)
        
        if len(self.head)-1 == 0:
            return 0
        return self.head[-1]

    def up(self, i:int):
        if i == 1:
            return
        if self.head[i]> self.head[i//2]:
            self.head[i], self.head[i//2] = self.head[i//2], self.head[i]
            return self.up(i//2)
        
    def down(self, i:int):
        left = i*2
        right = i*2 + 1
        largest = i

        if len(self.head)>left and self.head[i]<self.head[left]:
            largest = left

        if len(self.head)>right and self.head[largest]<self.head[right]:
            largest = right

        if largest != i:
            self.head[i], self.head[largest] = self.head[largest], self.head[i]
            return self.down(largest)

