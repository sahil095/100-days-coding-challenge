def removeDuplicates(self, nums: List[int]) -> int:
    j = 0
    n = len(nums)
    for i in range(n - 1):
        if nums[i] != nums[i + 1]:
            nums[j] = nums[i]
            j += 1
    nums[j] = nums[n - 1]
    return j + 1