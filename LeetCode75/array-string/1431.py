class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        biggest = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i]+extraCandies
            if biggest <= candies[i]:
                result.append(True)
                continue
            result.append(False)
        return result