class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        myDict = dict()
        for i in arr:
            if i in myDict:
                myDict[i] += 1
            else:
                myDict[i] = 1

        one = []
        for j in myDict.values():
            if j in one:
                return False
            else:
                one.append(j)
        return True