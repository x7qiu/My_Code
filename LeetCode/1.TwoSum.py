# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example
# Given nums = [2, 7, 11, 15], target = 9, return [0,1]




class Solution1(object):
    """ my 1st try,run time of 429ms
    
        sort the array, then loop through each element finding the complement using Binary search,
        and loop through the original array to find their index
    """
    def twoSum(self, nums, target):
        sort = sorted(nums)
        for (i, val) in enumerate(sort):
            x = self.BinarySearch(sort, 0, len(sort)-1, target-val)
            if i == x and type(x) == int:
                if sort[i] == sort[i+1]:
                    print [i, i+1]
                    return self.OriginalIndex(sort, nums, [i, i+1])
                else:
                    return
            if x:
                print [i,x]
                return self.OriginalIndex(sort, nums, [i, x])
            
    def BinarySearch(self, nums, left, right, target):
        if left > right:
            return False
        mid = (left + right)/2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.BinarySearch(nums, mid+1, right, target)
        if nums[mid] > target:
            return self.BinarySearch(nums, left, mid-1, target)

    def OriginalIndex(self, nums1, nums2, indices):
        ans = []
        for i in indices:
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    ans.append(j)
                if len(ans) == 2:
                    return ans
        return ans



class Solution2(object):
        """ my 2rd try, runtime of 45ms
            two-pass hashtable
        """
    def twoSum(self, nums, target):
        d = {}
        for (i, v) in enumerate(nums):
            if v in d:
                d[v].append(i)
            else:
                d[v] = [i]

        for val in d:
            want = target - val
            if want in d:
                if want == val and len(d[want]) == 1:
                    return  
                if want == val and len(d[want]) == 2:
                    return d[want]
                else:
                    ans = d[val]
                    ans.extend(d[want])
                    return ans

class Solution3(object):
    """ my 3rd try, runtime of 375ms
        one-pass hashtable, somehow slower than the two-pass version
    """
    def twoSum(self, nums, target):
        d = {}
        for (index,val) in enumerate(nums):
            want = target - val
            if (want in d) and (want != val):
                ans = d[want]
                ans.append(index)
                return ans
            if (want in d) and (want == val):
                ans = d[want]
                ans.append(index)
                return ans
            else:
                d[val] = [index]
                
                
                




S = Solution3()
print S.twoSum([2,7,11,15], 9)
print S.twoSum([2,2,11,15], 4)
print S.twoSum([2,3,11,15], 4)
print S.twoSum([3,2,4], 6)
print S.twoSum([3,2], 6)
print S.twoSum([3,2,3], 6)
