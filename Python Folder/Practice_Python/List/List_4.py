def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    length = len(nums)
    if length % 2 == 0:
        return (nums[length // 2 - 1] + nums[length // 2]) / 2
    else:
        return nums[length // 2]
nums1 = [1]
nums2 = [3, 4]
print("Median is:", findMedianSortedArrays(nums1, nums2))
