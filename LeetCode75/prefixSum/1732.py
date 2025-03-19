class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sumArr = [0]
        for i in range(len(gain)):
            sumArr.append(sumArr[i]+gain[i])
        print(gain, sumArr)
        return max(sumArr)