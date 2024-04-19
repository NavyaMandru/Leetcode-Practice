# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# Time complexity - O(m + n)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pnt1 = 0
        pnt2 = 0
        pnt = 0

        while pnt1 < m and pnt2 < n:
            if nums1[pnt] > nums2[pnt2]:
                for i in range(m+n-1, pnt, -1):
                    nums1[i] = nums1[i-1]
                nums1[pnt]= nums2[pnt2]

                pnt2 += 1
                pnt += 1
            else:
                pnt1 +=1
                pnt += 1
        
        while pnt2<n:
            for i in range(m+n-1, pnt, -1):
                nums1[i] = nums1[i-1]
            nums1[pnt]= nums2[pnt2]

            pnt2 += 1
            pnt += 1



        
        
