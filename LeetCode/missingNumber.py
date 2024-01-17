def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s_nums = sum(nums)
        sum_of_n = (n * (n + 1)) // 2
        missing_num = sum_of_n - s_nums
        return missing_num