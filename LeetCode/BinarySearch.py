def BinarySearch(nums, left, right, target):
    """ assum input sequence already sorted; if target not found, return False"""
    if left > right:
        return False
    mid = (left + right)/2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return BinarySearch(nums, mid+1, right, target)
    if nums[mid] > target:
        return BinarySearch(nums, left, mid-1, target)

a = [1,2,3,4,5,6,7]
print BinarySearch(a, 0, len(a) - 1, 5)


