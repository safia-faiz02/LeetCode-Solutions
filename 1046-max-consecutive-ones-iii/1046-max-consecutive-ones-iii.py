class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count_zero = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero += 1
            while count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len