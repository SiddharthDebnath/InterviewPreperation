class Solution:
    def containsDuplicate(self, nums):
        container = {}
        for i in nums:
            if i in container:
                return True
            else:
                container[i] = 1
        return False


print(Solution.containsDuplicate([1, 2, 3, 1]))
