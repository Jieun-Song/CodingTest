class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1Ex, n2Ex = list(set(nums1)), list(set(nums2))
        ns = n1Ex + n2Ex
        nsEx = set(ns)
        for i in nsEx:
            ns.remove(i)
        for j in ns:
            while j in n1Ex:
                n1Ex.remove(j)
            while j in n2Ex:
                n2Ex.remove(j)
        return [n1Ex, n2Ex]
