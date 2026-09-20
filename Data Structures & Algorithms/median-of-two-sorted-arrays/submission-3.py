class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        m = len(A)
        n = len(B)

        half = (m+n) // 2

        lo = 0
        hi = m

        while lo <= hi:

            i = (lo + hi) // 2 # partition on array A
            j = half - i # partition on array B

            Aleft = A[i-1] if i > 0 else float('-inf') # elem to the left of parition
            Aright = A[i] if i < m else float('inf') # elem to right of partition

            Bleft = B[j-1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')


            if Aleft <= Bright and Bleft <= Aright:

                if (m+n) % 2 == 0: # even case

                    return (max(Aleft, Bleft) + min(Bright, Aright)) /2
                
                else:

                    return min(Aright, Bright)

            elif Aleft > Bright:

                hi = i - 1

            else:

                lo = i + 1

        