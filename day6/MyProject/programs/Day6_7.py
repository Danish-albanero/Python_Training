#7 Container with most water
def maxArea(height):
    res = 0
    i = 0
    j = len(height) - 1
    while i < j:
        res = max(res, min(height[i], height[j]) * (j - i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return res
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
