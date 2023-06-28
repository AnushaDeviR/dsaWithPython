
def maxArea(self, height: List[int]) -> int:

    l, r = 0, len(height) - 1
    max_area = 0
    while l < r:
        width = r - l
        length = min(height[l], height[r])
        area = width * length
        print('current area:', area, 'max area:', max_area)
        max_area = max(area, max_area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

