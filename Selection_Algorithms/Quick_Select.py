import random
class Quick_Select():
    def __init__(self, nums):
        self.nums = nums
        self.first_index = 0
        self.last_index = len(nums) - 1

    def run(self, k):
        return self.select(self.first_index, self.last_index, k-1)

    def partition(self, first_index, last_index):
        pivot_index = random.randint(first_index, last_index)

        self.swap(pivot_index, last_index)

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        for i in range(first_index, last_index):
            

    def select(self, first_index, last_index, k):
        pivot_index = self.partition(first_index, last_index)