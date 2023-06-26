def sortColors(self, nums: List[int]) -> None:
    l, i = 0, 0
    r = len(nums) - 1

    while i <= r: 
        if nums[i] == 0: 
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
        elif nums[i] == 2: 
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
            i -= 1
        i += 1
