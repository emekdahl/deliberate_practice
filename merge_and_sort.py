def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """

    Do not return anything, modify nums1 in-place instead.
    """

    diff_length = len(nums1) - len(nums2)

    nums1[:] = nums1[0:diff_length]

    nums1[:] = nums1 + nums2

    nums1.sort()

# The reason why this wasn't working originally is because I was using nums1 instead of nums1[:] - good to know
