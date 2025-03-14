class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        tP = 0
        num = 0

        for sN in list(s):
            for tN in list(t[tP:]):
                tP += 1
                if sN == tN:
                    num += 1
                    break

        if num == len(s):
            return True
        return False