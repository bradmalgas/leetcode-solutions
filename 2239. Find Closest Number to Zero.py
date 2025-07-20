class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        smallest = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            val = abs(nums[i])
            if val < abs(smallest):
                smallest = curr
            elif val == abs(smallest):
                smallest = max(curr, smallest)
        return smallest
