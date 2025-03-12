class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        findZero = [0]
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        for i in flowerbed:
            if i == 0:
                findZero[len(findZero)-1] += 1
                continue
            findZero.append(0)

        print(findZero)
        compare =0
        if len(findZero) == 1 and findZero[0]== len(flowerbed):
            compare += (findZero[0]+1)//2

        else:
            for j in range(len(findZero)):
                if (j == 0) or (j == len(findZero)-1) or (findZero[j]==0):
                    compare += (findZero[j])//2 
                    continue
                compare += (findZero[j]-1)//2 

        if n <= compare:
            return True
        return False