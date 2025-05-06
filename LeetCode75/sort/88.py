class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        elif n == 0:
            return
        else:
            n1,n2 = 0,0

            while n1 < m + n2 and n2 < n:
                if nums1[n1] < nums2[n2]:
                    n1 += 1
                else:
                    nums1.insert(n1, nums2[n2])
                    nums1.pop()
                    n1 += 1
                    n2 += 1
            while n2 < n:
                nums1.insert(n1, nums2[n2])
                nums1.pop()
                n1 += 1
                n2 += 1
