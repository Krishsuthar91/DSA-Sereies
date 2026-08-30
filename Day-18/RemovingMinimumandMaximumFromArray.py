class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # Ensure min_index <= max_index
        if min_index > max_index:
            min_index, max_index = max_index, min_index

        # Option 1: Remove both from the front
        front = max_index + 1

        # Option 2: Remove both from the back
        back = n - min_index

        # Option 3: Remove one from the front and one from the back
        both = (min_index + 1) + (n - max_index)

        return min(front, back, both)