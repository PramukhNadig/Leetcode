class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = list(map(int, version1.split('.')))
        nums2 = list(map(int, version2.split('.')))
        
        if len(nums1) < len(nums2):
            nums1 += [0] * (len(nums2) - len(nums1))
        elif len(nums1) > len(nums2):
            nums2 += [0] * (len(nums1) - len(nums2))
        
        for rev1, rev2 in zip(nums1, nums2):
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        return 0
