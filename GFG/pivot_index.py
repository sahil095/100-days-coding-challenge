def pivotIndex(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    left = 0
    pivot = 0
    right = sum(nums[1:])
    while pivot < n - 1 and right != left:
        pivot += 1
        right -= nums[pivot]
        left += nums[pivot - 1]

    return pivot if left == right else -1 