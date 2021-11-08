import statistics

nums1 = [2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
nums2 = [1, 12, 13, 14, 15, 16, 17, 18, 19, 20]

Durchschnitt = statistics.median(nums1 + nums2)
print(Durchschnitt)
