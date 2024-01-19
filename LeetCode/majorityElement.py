def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    uniq = set(nums)
    for i in uniq:
        if nums.count(i) > n//2:
            return i