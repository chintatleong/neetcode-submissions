class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        # pointers of A
        l, r = 0, len(A) - 1

        while True:
            # find cut of A
            A_m = (l+r) // 2

            # find cut of B
            remain = half - (A_m + 1)
            B_m = half - A_m - 2

            # left of the cut and right of the cut
            Aleft = A[A_m] if A_m >= 0 else float("-inf")               # ser l bound for A
            Aright = A[A_m + 1] if A_m + 1 < len(A) else float("inf")   # set r bound for A

            Bleft = B[B_m] if B_m >= 0 else float("-inf")               # set l bound for B
            Bright = B[B_m + 1] if B_m + 1 < len(B) else float("inf")   # set r bound for B

            if Aleft > Bright:   # search L half of A
                r = A_m - 1
            
            elif Bleft > Aright:   # search R half of A
                l = A_m + 1

            else:
                if total % 2:
                    return min(Aright, Bright)      # min of the two

        return (max(Aleft, Bleft) + min(Aright, Bright)) / 2        # similar idea like minHeap, even of max of smaller part and min of bigger part




        
