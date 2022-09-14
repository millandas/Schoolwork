def quicksort(array):
    length = len(array)
    if length<=1:
        return(array)
    else:
        pivot = array.pop()
    greater = []
    less = []
    for nums in array:
        if nums>pivot:
            greater.append(nums)
        else:
            less.append(nums)
    return quicksort(less)+ [pivot]+ quicksort(greater)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums3 = nums1+nums2
        sorted = quicksort(nums3)
        if len(sorted)%2 == 1:
            index = len(sorted)//2 +1
            return(sorted[index-1])
        elif len(sorted)%2 == 0:
            index1 = len(sorted)//2
            index2 = len(sorted)//2 +1
            median = (sorted[index1-1]+sorted[index2-1])/2
            return(median)


