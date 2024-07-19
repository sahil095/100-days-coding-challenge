def maxOperations(self, nums: List[int], k: int) -> int:
    nums = sorted(nums)
    ans = 0
    i = 0
    j = len(nums)-1
    while i < j:
        temp_sum = nums[i] + nums[j]
        if temp_sum == k:
            ans += 1
            i += 1
            j -= 1
        elif temp_sum < k:
            i += 1
        else:
            j -= 1
    return ans