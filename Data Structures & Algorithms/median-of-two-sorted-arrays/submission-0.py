class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i , j = 0, 0
        new = []

        m = len(nums1)
        n = len(nums2)

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                new.append(nums1[i])
                i += 1
            
            else:
                new.append(nums2[j])
                j += 1

            if i == m and j < n:
                while j != n:
                    new.append(nums2[j])
                    j += 1
        
            if i < m and j == n:
                while i != m:
                    new.append(nums1[i])
                    i += 1

        length = len(new) 

        if length % 2 == 1:
            m = length//2
            median = new[m]
        
        else:
            m = length//2
            median = (new[m] + new[m-1])/2

        return float(median)
            