class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums, reverse=True)
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i - 1]:
                return True
        return False